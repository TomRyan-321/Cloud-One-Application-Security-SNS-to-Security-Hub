import boto3
import copy
import datetime
import json
import re


def lambda_handler(event, context):

    for record in event["Records"]:

        securityhub = boto3.client("securityhub")
        message = json.loads(record["Sns"]["Message"])
        awsaccountid = boto3.client("sts").get_caller_identity()["Account"]
        region = boto3.session.Session().region_name
        findings = []
        for item in message:
            date = datetime.datetime.utcnow().isoformat("T") + "Z"
            url = item["dashboard_link"]
            action = item["action"]
            group = item["group"]
            severity = item["severity"].upper()
            eventid = re.search(r"(?<=event_id=).*?(?=\&)", url).group(0)
            eventtype = item["event_type"]
            finding = {
                "SchemaVersion": "2018-10-08",
                "AwsAccountId": awsaccountid,
                "CreatedAt": date,
                "Description": f"Application Security Event, event type: {eventtype}",
                "GeneratorId": "TM-CloudOne-ApplicationSecurity",
                "Id": eventid,
                "ProductArn": f"arn:aws:securityhub:{region}:{awsaccountid}:product/{awsaccountid}/default",
                "Remediation": {
                    "Recommendation": {
                        "Text": "Application Security Console URL",
                        "Url": url,
                    }
                },
                "Resources": [
                    {
                        "Type": "Other",
                        "Id": group,
                        "Details": {"Other": {"Group": group, "Action": action}},
                    }
                ],
                "Severity": {"Label": severity},
                "Title": f"Cloud Application Security {action} the following event type: {eventtype} for Group Name: {group}",
                "Types": [
                    f"TTPs/Common Weakness Enumeration/{eventtype}",
                    "Unusual Behaviors",
                ],
                "UpdatedAt": date,
            }
            findings.append(copy.deepcopy(finding))
        response = securityhub.batch_import_findings(Findings=findings)
        print(json.dumps(response))
