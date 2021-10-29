#!/bin/bash
echo Easy Github push generator
echo Enter Commit Tilte:
read commit


git add . && git commit -m "$commit"
