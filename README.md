# Cloud-One-Application-Security-SNS-to-Security-Hub
## Description
This AWS SAM (Serverless Application Model) deployment configures the required resources to send Trend Micro's Cloud One Application Security events to AWS Security Hub.

![Screenshot](doc/screenshot.png)


## Prerequisites
1. **Install AWS SAM CLI**
    - Visit [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) for detailed instructions for your Operating System.
    - Configure your [AWS Credentials](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html) for use with AWS SAM CLI.
2. **Configure Application Security SNS integration to obtain the external ID value**
    - Access to the Cloud One - Application Security console with administrative privileges to create a new integration.

## Installation

### From AWS SAM CLI

1. Open the Application Security Console - Select Integrations - Select Amazon SNS, select and copy the `External ID` value as this will be needed when entering the parameters. Leave the rest of the values blank for now, details for these values will be available after completing the next steps.
2. Clone this repository from [Github](https://github.com/TomRyan-321/Cloud-One-Application-Security-SNS-to-Security-Hub).
3. Using your terminal navigate to the `Cloud-One-Application-Security-SNS-to-Security-Hub` folder contained within the above cloned repository. Example: `User@Host:cd ~/Cloud-One-Application-Security-SNS-to-Security-Hub/`
4. Deploy the SAM template in guided mode. Example: `sam deploy --guided`
5. Fill in the external ID paramater with the value you copied in step 1.
6. Select `Yes` by press `Y` to the following prompts: `Confirm changes before deploying`, `Allow SAM CLI IAM role creation`
7. Optionally save the above parameters to a configuration file when promtped.
8. Review the resources to be created/updated and select `Yes` by pressing `Y` to deploy the solution.
9. Once deployment finishes, it output will provide the rest of the values required for finishing the integration within the Application Security console.
