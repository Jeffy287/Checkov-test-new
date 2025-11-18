provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "test_lambda" {
  function_name = "test_lambda"
  handler       = "index.handler"
  runtime       = "python3.8"
  filename      = "lambda_function_payload.zip"
  role          = "arn:aws:iam::123456789012:role/execution_role:2" # <- This should FAIL
}
