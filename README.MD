[![CodeQL](https://github.com/nacifyas/users-demo/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/nacifyas/users-demo/actions/workflows/codeql-analysis.yml)
[![Build](https://github.com/nacifyas/users-demo/actions/workflows/flake8-mypy-build.yml/badge.svg)](https://github.com/nacifyas/users-demo/actions/workflows/flake8-mypy-build.yml)

Microservice corresponding to manager users.

Follow the correspondig steps at the [API Gateway Microservice](https://github.com/nacifyas/gateway-edm-demo/) to install and use.

The functionality of this MS is to exclusivly handle *users* and its CRUD related operations.

This MS uses redis as its primary database, and its event stream for events sourcing.
