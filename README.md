# Hotel Front Desk Web Application using AWS 

The purpose of this homework assignment is to get students an opportunity to build a cloud application using EC2 and utilize some of the AWS tools.


# Table of Contents

- [AWS Account Setup](#aws-account-setup)
  - [How to Create an AWS Account](#how-to-create-an-aws-account)
  - [How to Create an IAM Role in AWS](#how-to-create-an-iam-role-in-aws)
  - [How to Create a VPC in AWS](#how-to-create-a-vpc-in-aws)
  - [How to Create an EC2 Instance in AWS](#how-to-create-an-ec2-instance-in-aws)
  - [How to Create an Internet Gateway in AWS](#how-to-create-an-internet-gateway-in-aws)
  - [How to Create a Route Table in AWS](#how-to-create-a-route-table-in-aws)
- [Connecting to the EC2 Instance](#connecting-to-the-ec2-instance)
  - [Option 1: Connect using SSH from Local](#option-1-connect-using-ssh-from-local)
  - [Option 2: Connect using the AWS CLI](#option-2-connect-using-the-aws-cli)
- [Creating Directories in EC2 Instance](#creating-directories-in-ec2-instance)
  - [Option 1: Using Terminal or SSH](#option-1-using-terminal-or-ssh)
  - [Option 2: Using AWS S3](#option-2-using-aws-s3)
- [Creating Files in EC2 Instance](#creating-files-in-ec2-instance)
  - [Option 1: Using Terminal or SSH](#option-1-using-terminal-or-ssh)
  - [Option 2: Uploading Files](#option-2-uploading-files)
  - [Option 3: Using AWS S3](#option-3-using-aws-s3)
- [Sending Files to EC2 Instance](#sending-files-to-ec2-instance)
  - [Option 1: Using Terminal or SSH](#using-terminal-or-ssh)
  - [Option 2: Using AWS S3](#using-aws-s3)
  - [Option 3: Using FileZilla](#using-filezilla)
- [Deploying Python Web Application Project](#deploying-python-web-application-project)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)



# AWS Account Setup

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

<details>
  <summary> How to Create a VPC in AWS </summary>

  A Virtual Private Cloud (VPC) is a logically isolated section of the AWS Cloud where you can launch AWS resources. Follow the steps below to create a VPC:

  ### 1. Navigate to the VPC Dashboard

  - Go to the AWS Management Console and navigate to the VPC service.

  ### 2. Click on "Your VPCs"

  - In the VPC dashboard, click on "Your VPCs" in the navigation pane.

  ### 3. Click on "Create VPC"

  - Click the "Create VPC" button to initiate the VPC creation process.

  ### 4. Enter VPC Details

  - Provide a name and CIDR block for your VPC.
  - Optionally, configure IPv6 CIDR blocks and other advanced settings.

  ### 5. Configure Subnets

  - Define subnets within your VPC. Specify the CIDR block for each subnet and ensure they are associated with the VPC.

  ### 6. Configure Route Tables

  - Create and configure route tables for your VPC. Define routes for traffic leaving and entering the VPC.

  ### 7. Configure Security Groups and Network ACLs

  - Set up security groups to control inbound and outbound traffic to your instances.
  - Configure Network Access Control Lists (NACLs) for additional network-level security.

  ### 8. Configure Internet Gateway (Optional)

  - If you want your VPC to communicate with the internet, create and attach an Internet Gateway.

  ### 9. Review and Create

  - Review the configuration details for your VPC.
  - Click "Create VPC" to complete the process.

  **Congratulations!** You have successfully created a VPC in AWS. Your VPC is now ready to host and isolate AWS resources within your defined network.

</details>

<details>
  <summary>How to Create an EC2 Instance in AWS</summary>

  An EC2 instance is a virtual server in the AWS cloud. Follow the steps below to create an EC2 instance:

  ### 1. Navigate to the EC2 Dashboard

  - Go to the AWS Management Console and navigate to the EC2 service.

  ### 2. Click on "Launch Instance"

  - In the EC2 dashboard, click on "Launch Instance" to initiate the instance creation process.

  ### 3. Choose an Amazon Machine Image (AMI)

  - Select an AMI that suits your application requirements. This image will serve as the base for your instance.

  ### 4. Choose an Instance Type

  - Choose the instance type based on the computing resources needed for your application.

  ### 5. Configure Instance Details

  - Specify configuration details such as the number of instances, network settings, and user data.

  ### 6. Add Storage

  - Configure the storage settings for your instance, including the root volume and any additional volumes.

  ### 7. Configure Security Groups

  - Define security groups to control inbound and outbound traffic to your instance.

  ### 8. Review and Launch

  - Review the configuration settings and click "Launch" to proceed.

  ### 9. Create or Select Key Pair

  - Choose an existing key pair or create a new one. This key pair is crucial for accessing your instance securely.

  ### 10. Launch Instances

  - Click "Launch Instances" to create and launch your EC2 instances.

  **Congratulations!** You have successfully created an EC2 instance in AWS. Your instance is now running and ready for use.

</details>

<details>
  <summary>How to Create an Internet Gateway in AWS</summary>

  An Internet Gateway enables communication between instances in your Virtual Private Cloud (VPC) and the internet. Follow the steps below to create an Internet Gateway:

  ### 1. Navigate to the VPC Dashboard

  - Go to the AWS Management Console and navigate to the VPC service.

  ### 2. Click on "Internet Gateways" in the Navigation Pane

  - In the VPC dashboard, click on "Internet Gateways" in the left navigation pane.

  ### 3. Click on "Create Internet Gateway"

  - Click the "Create Internet Gateway" button to initiate the Internet Gateway creation process.

  ### 4. Name the Internet Gateway (Optional)

  - Optionally, provide a name for the Internet Gateway to help identify it.

  ### 5. Click on "Create Internet Gateway"

  - Click the "Create Internet Gateway" button to complete the process.

  ### 6. Attach Internet Gateway to VPC

  - In the Internet Gateways dashboard, select the Internet Gateway you just created.
  - Click on "Actions" and choose "Attach to VPC."
  - Select the VPC to which you want to attach the Internet Gateway.

  **Congratulations!** You have successfully created and attached an Internet Gateway to your VPC. Your VPC can now communicate with the internet through this gateway.

</details>

<details>
  <summary>How to Create a Route Table in AWS</summary>

  A Route Table in AWS is used to define rules for routing network traffic within a Virtual Private Cloud (VPC). Follow the steps below to create a Route Table:

  ### 1. Navigate to the VPC Dashboard

  - Go to the AWS Management Console and navigate to the VPC service.

  ### 2. Click on "Route Tables" in the Navigation Pane

  - In the VPC dashboard, click on "Route Tables" in the left navigation pane.

  ### 3. Click on "Create Route Table"

  - Click the "Create Route Table" button to initiate the Route Table creation process.

  ### 4. Name the Route Table

  - Provide a name for the Route Table to help identify its purpose.

  ### 5. Associate the Route Table with a VPC

  - In the "Associations" tab, click on "Edit associations."
  - Select the subnets you want to associate with the Route Table.

  ### 6. Add Routes

  - In the "Routes" tab, click on "Edit routes."
  - Add routes to define how network traffic should be directed.

  ### 7. Save Changes

  - Save the changes to create and configure the Route Table.

  **Congratulations!** You have successfully created a Route Table in AWS and configured routing rules for your VPC.

</details>

# Connecting to the EC2 Instance

<details>
  <summary>Option 1: Connect using SSH from Local</summary>

  Connecting to your EC2 instance using SSH from your local machine allows you to access and manage the instance securely.

  ### Prerequisites
  - An EC2 instance with SSH key pair
  - The private key (.pem) file associated with the key pair

  ### Steps
  1. Open a terminal on your local machine.
  2. Use the following command to connect to your EC2 instance. Replace `your-instance-ip` with the actual public IP address of your EC2 instance and `your-key.pem` with the path to your private key file.

      ```bash
      ssh -i /path/to/your-key.pem ec2-user@your-instance-ip
      ```

  3. You are now connected to your EC2 instance via SSH.

</details>

<details>
  <summary>Option 2: Connect using the AWS CLI</summary>

  You can also connect to your EC2 instance using the AWS Command Line Interface (CLI), providing a convenient way to manage your AWS resources.

  ### Prerequisites
  - AWS CLI installed on your local machine
  - AWS credentials configured on your machine

  ### Steps
  1. Open a terminal on your local machine.
  2. Use the following command to connect to your EC2 instance. Replace `your-instance-id` with the actual ID of your EC2 instance.

      ```bash
      aws ec2-instance-connect send-ssh-public-key --instance-id your-instance-id --availability-zone your-instance-availability-zone --instance-os-user ec2-user --ssh-public-key file://path/to/your-public-key.pub
      ```

  3. You are now connected to your EC2 instance using the AWS CLI.

</details>

Adjust the content as needed, and make sure to replace placeholders such as `your-instance-ip`, `your-key.pem`, `your-instance-id`, `your-instance-availability-zone`, and `path/to/your-public-key.pub` with your actual information.

# Creating Directories in EC2 Instance

<details>
  <summary>Option 1: Using Terminal or SSH</summary>

  You can create directories directly on your EC2 instance using the terminal or SSH connection.

  ### Steps
  1. Connect to your EC2 instance using SSH.
  2. Use terminal commands to navigate to the desired location where you want to create the directory.
  3. Use the `mkdir` command to create a new directory. For example:

      ```bash
      mkdir new_directory
      ```

  4. Verify that the directory has been successfully created.

</details>

<details>
  <summary>Option 2: Using AWS S3</summary>

  Another option is to use AWS S3 to store and retrieve directories on your EC2 instance.

  ### Steps
  1. Upload the directory (with its contents) to an S3 bucket using the AWS Management Console or AWS CLI.
  2. Connect to your EC2 instance using SSH.
  3. Use the AWS CLI to download the directory from S3 to your EC2 instance. For example:

      ```bash
      aws s3 sync s3://your-bucket-name/path/to/directory /path/to/local/
      ```

  4. Verify that the directory has been successfully downloaded.

</details>

Adjust the content as needed, and make sure to replace placeholders such as `new_directory`, `your-bucket-name`, `/path/to/directory`, and `/path/to/local/` with your actual information.

# Creating Files in EC2 Instance

<details>
  <summary>Option 1: Using Terminal or SSH</summary>

  You can create files directly on your EC2 instance using the terminal or SSH connection.

  ### Steps
  1. Connect to your EC2 instance using SSH.
  2. Use terminal commands to navigate to the desired directory where you want to create the file.
  3. Use a text editor, such as `nano`, `vim`, or `emacs`, to create and edit files. For example:

      ```bash
      nano filename.txt
      ```

  4. Enter your text in the editor, save, and exit.

</details>

<details>
  <summary>Option 2: Uploading Files</summary>

  You can upload files from your local machine to your EC2 instance.

  ### Steps
  1. Use a tool like `scp` or an SFTP client to transfer files from your local machine to the EC2 instance. For example:

      ```bash
      scp /path/to/local/file.txt ec2-user@your-instance-ip:/path/to/remote/
      ```

  2. Connect to your EC2 instance using SSH.
  3. Verify that the file has been successfully transferred.

</details>

<details>
  <summary>Option 3: Using AWS S3</summary>

  Another option is to use AWS S3 to store and retrieve files on your EC2 instance.

  ### Steps
  1. Upload the file to an S3 bucket using the AWS Management Console or AWS CLI.
  2. Connect to your EC2 instance using SSH.
  3. Use the AWS CLI to download the file from S3 to your EC2 instance. For example:

      ```bash
      aws s3 cp s3://your-bucket-name/path/to/file.txt /path/to/local/
      ```

  4. Verify that the file has been successfully downloaded.

</details>

Adjust the content as needed, and make sure to replace placeholders such as `filename.txt`, `your-instance-ip`, `/path/to/local/file.txt`, `your-bucket-name`, and `/path/to/remote/` with your actual information.

# Sending Files to EC2 Instance

<details>
  <summary>Option 1: Using Terminal or SSH</summary>

  You can send files directly to your EC2 instance using the terminal or SSH connection.

  ### Steps
  1. Connect to your EC2 instance using SSH.
  2. Use terminal commands to navigate to the destination location on your EC2 instance.
  3. Use the `scp` command to securely copy files from your local machine to the EC2 instance. For example:

      ```bash
      scp /path/to/local/file.txt ec2-user@your-instance-ip:/path/on/ec2/
      ```

  4. Verify that the file has been successfully copied.

</details>

<details>
  <summary>Option 2: Using AWS S3</summary>

  Another option is to use AWS S3 to store and retrieve files on your EC2 instance.

  ### Steps
  1. Upload the file to an S3 bucket using the AWS Management Console or AWS CLI.
  2. Connect to your EC2 instance using SSH.
  3. Use the AWS CLI to download the file from S3 to your EC2 instance. For example:

      ```bash
      aws s3 cp s3://your-bucket-name/path/to/file.txt /path/on/ec2/
      ```

  4. Verify that the file has been successfully downloaded.

</details>

<details>
  <summary>Option 3: Using FileZilla</summary>

  FileZilla is a popular graphical SFTP client that simplifies file transfer to and from your EC2 instance.

  ### Steps

  #### 1. Download and Install FileZilla Client

  - Download FileZilla Client from the [official website](https://filezilla-project.org/) (make sure to download the client version, not the server version).
  - Install FileZilla Client on your local machine.

  #### 2. Gather EC2 Instance Information

  - Open the AWS Management Console.
  - Navigate to the EC2 service.
  - Note the following information:
    - **Public IP address** of your EC2 instance.
    - **Username** (usually `ec2-user` for Amazon Linux instances).
    - **Private key** (.pem file) used for authentication.

  #### 3. Configure FileZilla

  - Open FileZilla and go to `File` > `Site Manager`.
  - Click on `New Site` and enter a name for your EC2 instance.
  - Set the `Protocol` to `SFTP - SSH File Transfer Protocol`.
  - Enter the EC2 instance's **Public IP address** as the `Host`.
  - Set the `Port` to `22`.
  - Select `Key file` as the logon type and browse to your EC2 instance's **Private key** (.pem file).
  - Click `Connect` to save the configuration.

  #### 4. Connect to the EC2 Instance

  - In FileZilla, select the EC2 instance from the `Site Manager` or click `File` > `Site Manager` and select your EC2 site.
  - Click `Connect`.

  #### 5. Transfer Files

  - Once connected, you'll see the local files on the left and the remote files on the right.
  - Navigate to the destination directory on the EC2 instance (right side).
  - Select the files on your local machine (left side) that you want to transfer.
  - Drag and drop the selected files to the desired directory on the EC2 instance.

  #### 6. Verify Transfer

  - After the transfer is complete, verify that the files appear in the correct destination on the EC2 instance.

  **Note:** Ensure that you've set the correct file and directory permissions on the EC2 instance for FileZilla to access and transfer files.

</details>

# Deployment

<details>
  <summary>Deploying Python Web Application Project</summary>

  This guide provides steps to deploy a Python web application project to an EC2 instance.

  ### 1. Download the Repository

  - Clone or download the repository to your local machine.

  ### 2. Run Demo App Locally

  - Open the terminal in Visual Studio Code.
  - Run the demo app by executing the following commands:
    ```bash
    python run.py
    ```
  - Click on the first HTTP link (usually http://127.0.0.1:5000) to open the web app.
  - Stop the web app by pressing `CTRL+C`.
  - Save the project dependencies to `requirements.txt`:
    ```bash
    pip freeze > requirements.txt
    ```

  ### 3. Connect to the EC2 Instance

  - SSH into the EC2 instance from your local device.

  ### 4. Upload Files Using FileZilla

  - Use FileZilla to upload the project files to the EC2 instance.

  ### 5. Check Python Version

  - In the EC2 terminal, check the Python version:
    ```bash
    python --version
    ```
    To exit the Python interpreter, type `exit()`.

  ### 6. Create a Directory and Set Up Virtual Environment

  - Create a directory and navigate to it:
    ```bash
    mkdir your_directory_name
    cd your_directory_name
    ```

  - Create a Python virtual environment:
    ```bash
    python3 -m venv venv
    ```

  - Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

  ### 7. Install Project Dependencies

  - Install the project dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

  ### 8. Update Pip

  - Upgrade pip to the latest version:
    ```bash
    pip install --upgrade pip
    ```

  ### 9. Run the Web App

  - Start the web app:
    ```bash
    python run.py
    ```

  ### 10. Access the Website

  - Open your browser and go to your EC2 instance's public IP address with port 5000 (e.g., http://1.2.3.4:5000).

  ### 11. Adjust Security Group Rules (if needed)

  - If the website doesn't load, check your EC2 instance's security group.
  - Add a custom TCP rule for port 5000 with source `0.0.0.0/0` to allow external access.

  Now, your Python web application is deployed on the EC2 instance. Customize the commands based on your project structure and requirements.

</details>

# Contributors

A big shoutout to the fantastic contributors who have made valuable contributions to this project!

### Deep Bhakta
- **Email:** [deepbhakta06@gmail.com](mailto:deepbhakta06@gmail.com)
- **GitHub:** [deep06bhakta](https://github.com/deep06bhakta)
- **LinkedIn:** [Deep Bhakta](https://www.linkedin.com/in/deep-bhakta-07355a172/)

### Branden Zamora
- **Email:** [branden.z1229@gmail.com](mailto:branden.z1229@gmail.com)
- **GitHub:** [branden12](https://github.com/branden12)
- **LinkedIn:** [Branden Zamora](https://www.linkedin.com/in/brandenz29/)

### Brian Contreras
- **Email:** N/A
- **GitHub:** N/A
- **LinkedIn:** [Brian Contreras](https://www.linkedin.com/in/contrerasbrian/)

If you're interested in contributing to this project or connecting with our contributors, feel free to reach out! Your contributions and support are highly appreciated.

<!-- Add any additional information or instructions for contributors below this line -->



