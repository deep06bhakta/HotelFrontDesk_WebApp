# Hotel Front Desk Web Application using EC2 Instance

The purpose of this homework assignment is to get students an opportunity to build a cloud application using EC2 and utilize some of the AWS tools.


# Table of Contents

- [How to Create an AWS Account](#how-to-create-an-aws-account)
    - [Navigate to the AWS Sign-Up Page](#1-navigate-to-the-aws-sign-up-page)
    - [Provide your Email Address](#2-provide-your-email-address)
    - [Enter Account Information](#3-enter-account-information)
    - [Contact Information Verification](#4-contact-information-verification)
    - [Enter Payment Information](#5-enter-payment-information)
    - [Verify your Identity](#6-verify-your-identity)
    - [Choose a Support Plan](#7-choose-a-support-plan)
    - [Complete Sign-Up](#8-complete-sign-up)
    - [Account Activation](#9-account-activation)

- [How to Create an IAM Role in AWS](#how-to-create-an-iam-role-in-aws)
    - [Navigate to the IAM Console](#1-navigate-to-the-iam-console)
    - [Select "Roles" in the Navigation Pane](#2-select-roles-in-the-navigation-pane)
    - [Click on "Create Role"](#3-click-on-create-role)
    - [Choose the Trusted Entity Type](#4-choose-the-trusted-entity-type)
    - [Select Use Case and Permissions](#5-select-use-case-and-permissions)
    - [Attach Policies](#6-attach-policies)
    - [Configure Tags (Optional)](#7-configure-tags-optional)
    - [Review and Name the Role](#8-review-and-name-the-role)
    - [Access and Use the Role](#9-access-and-use-the-role)

- [Additional Sections (if applicable)](#additional-sections-if-applicable)
    - [Section 1](#21-section-1)
    - [Section 2](#22-section-2)

- [Contributing](#contributing)

- [License](#license)

<details>
  <summary><strong>How to Create an AWS Account</strong></summary>

  Amazon Web Services (AWS) provides a robust cloud computing platform, and creating an AWS account is the first step to leverage its services. Follow the steps below to set up your AWS account:

  ### 1. Navigate to the AWS Sign-Up Page

  - Visit the [AWS sign-up page](https://aws.amazon.com/).
  - Look for the "Sign Up" button on the top right corner of the page and click on it.

  ### 2. Provide your Email Address

  - Enter a valid email address that you will use for your AWS account. This email will be associated with the account and used for communication from AWS.

  ### 3. Enter Account Information

  - Fill in the required information, including your name, company name (if applicable), and a secure password. Make sure to choose a strong password to enhance the security of your AWS account.

  ### 4. Contact Information Verification

  - AWS will ask you to enter your contact number. Provide a valid phone number as AWS may use it for security purposes. You will receive a verification code on this number.

  ### 5. Enter Payment Information

  - To access certain AWS services, you need to provide payment information. AWS offers a free tier with limited resources for the first 12 months, but you'll still need to enter payment details.

  ### 6. Verify your Identity

  - To enhance security, AWS may ask for additional identity verification. This may include entering a CAPTCHA or using a multi-factor authentication (MFA) device.

  ### 7. Choose a Support Plan

  - Select a support plan based on your preferences. AWS offers various plans, including a free plan with basic support.

  ### 8. Complete Sign-Up

  - Review your information, agree to the terms and conditions, and click on the "Create Account and Continue" button to complete the sign-up process.

  ### 9. Account Activation

  - You will receive an email from AWS asking you to confirm your email address. Click on the confirmation link provided in the email to activate your AWS account.

  **Congratulations!** You have successfully created an AWS account. You can now log in to the AWS Management Console and start exploring the wide range of cloud services offered by AWS.

</details>

<details>
  <summary><strong>How to Create an IAM Role in AWS</strong></summary>

  IAM roles in AWS are used to delegate permissions to entities that you trust. Follow the steps below to create an IAM role:

  ### 1. Navigate to the IAM Console

  - Go to the AWS Management Console and navigate to the IAM (Identity and Access Management) service.

  ### 2. Select "Roles" in the Navigation Pane

  - In the IAM dashboard, select "Roles" from the left navigation pane.

  ### 3. Click on "Create Role"

  - Click the "Create Role" button to initiate the role creation process.

  ### 4. Choose the Trusted Entity Type

  - Select the trusted entity type. This is typically the AWS service that will assume the role. Choose the service or entity that will assume this role.

  ### 5. Select Use Case and Permissions

  - Choose a use case scenario that best describes your use of this role, and then click "Next: Permissions."

  ### 6. Attach Policies

  - Search and attach policies that define the permissions for the role. These policies determine what actions can be performed by the role.

  ### 7. Configure Tags (Optional)

  - Optionally, you can add tags to the role for better organization and management. Click "Next: Tags" if you want to add tags.

  ### 8. Review and Name the Role

  - Provide a meaningful name and description for your role. Review the configuration settings and click "Create Role" to complete the process.

  ### 9. Access and Use the Role

  - Once the role is created, you can find it in the IAM dashboard under "Roles." To use the role, note its Amazon Resource Name (ARN) and configure the entity that will assume this role, such as an EC2 instance or an AWS Lambda function.

  **Congratulations!** You have successfully created an IAM role in AWS. This role can now be assumed by trusted entities to access AWS resources based on the assigned permissions.

</details>






