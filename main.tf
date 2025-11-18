provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "test_lambda" {
  function_name = "test_lambda"
  handler       = "index.handler"
  runtime       = "python3.8"
  filename      = "lambda_function_payload.zip"
  role          = "arn:aws:iam::123456789012:role/execution_role:2" # <- Version-pinned ARN (should FAIL)
}

resource "aws_lambda_function" "ok_lambda" {
  function_name = "ok_lambda"
  handler       = "index.handler"
  runtime       = "python3.8"
  filename      = "lambda_function_payload.zip"
  role          = "arn:aws:iam::123456789012:role/execution_role" # <- NOT version-pinned (should PASS)
}
