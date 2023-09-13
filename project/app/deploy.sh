#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <version> <commit-hash>"
  exit 1
fi

version="$1"
commit_hash="$2"
# git log --oneline | grep -q "$commit_hash"

#   if [ $? -eq 0 ]; then
#     echo "Hash $commit_hash found in Git log."
#   else
#     echo "Hash $hash not found in Git log."
#   fi

image_name="chat app"

tag="$version"

git tag "$tag" "$commit_hash"

git push origin "$tag"

docker build -t "$image_name:$tag" .

echo "Deployment completed successfully."
