# serverless-spotify-toplists

Production-style starter for an AWS Lambda (Python 3.13) that writes a CSV to S3 on a schedule (EventBridge).

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
make test
make local-run
```
Outputs: `samples/sample-output.csv`

## AWS (manual)
- Create S3 bucket (e.g. `your-bucket`), optional prefix `results/`
- Create Lambda (Python 3.13), handler `lambda_handler.handler`
- Env vars: `OUTPUT_BUCKET`, `OUTPUT_PREFIX=results/`
- `make zip-lambda` → upload `build/lambda.zip`
- Create EventBridge rule (cron) → target the Lambda
