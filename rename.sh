#! /bin/bash

new_project_name="${1}"

if [[ -z $new_project_name ]]
then
  echo "ERROR: Please provide a new project name. Example: ./rename.sh my_project";
  exit 1;
fi

find project_name -type f -exec sed -i "s/project_name/$new_project_name/g" {} \;
find tests -type f -exec sed -i "s/project_name/$new_project_name/g" {} \;
sed -i "s/project_name/$new_project_name/g" pyproject.toml;
mv project_name $new_project_name
