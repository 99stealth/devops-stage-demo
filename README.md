# DevOps Stage Demo

- Go to CloudFormation console and create stack with `generic_ecs.json`
- Deploy `return_free_priority_lambda.json`
- After two previous stacks are deployed - deploy `get_free_priority.json`
- Open the `get_free_priority.json` stack `Output` and check Value of `FreePriorityID`