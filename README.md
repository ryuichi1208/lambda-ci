# lambda-ci

A program built up to program lambda.

At the time of deployment, deploy by incorporating a workflow that requires CI.The sample code is borrowed from the tutorial.

### CI-Flow

``` yaml
on:
  push:
    branches:
      - master

name: Auto Deploy to AWS Lambda

jobs:
  deploy:
    name: Auto Deploy
    runs-on: ubuntu-18.04
    steps:
      - uses: actions/checkout@master

      - name: Setup Node.js
        uses: actions/setup-node@v1
        with:
          node-version: '10.x'

      - name: Install Dependencies
        run: |
          npm install serverless -g
          npm install

      - name: Deploy to Lambda
        run: sls deploy
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}

      - name: Execute Lambda
        run: sls invoke -f slack
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}

      - name: Notify result to slack
        uses: homoluctus/slatify@master
        if: always()
        with:
          type: ${{ job.status }}
          job_name: '*Deploy Lambda*'
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
```
