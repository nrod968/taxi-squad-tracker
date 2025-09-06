#!/bin/bash
poetry run pytest "$@"
EXIT_CODE=$?
if [ $EXIT_CODE -eq 5 ]; then
    exit 0  # no tests collected → allow commit
else
    exit $EXIT_CODE  # preserve real failures
fi
