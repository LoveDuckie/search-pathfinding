#!/usr/bin/env bash
<<EOF

   Tool \ Shell Scripts \ Run \ Rename

   Rename the code files and references to "python-project-template" in the repository.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

export LC_ALL=C
export LC_ALL=en_US.UTF-8

# Function to rename files and directories
rename_files_and_directories() {
    for item in $(find . -depth -name "*$PROJECT_NAME*"); do
        new_item=$(echo "$item" | sed "s/$PROJECT_NAME/$new_project_name/g")
        mv "$item" "$new_item"
    done
    
    PROJECT_NAME_UPPERCASE=$(echo $PROJECT_NAME | tr '[:lower:]' '[:upper:]')
    NEW_PROJECT_NAME_UPPERCASE=$(echo $new_project_name | tr '[:lower:]' '[:upper:]')
    for item in $(find . -depth -name "*$PROJECT_NAME_UPPERCASE*"); do
        new_item=$(echo "$item" | sed "s/$PROJECT_NAME_UPPERCASE/$NEW_PROJECT_NAME_UPPERCASE/g")
        mv "$item" "$new_item"
    done
}

# Function to replace text within files
replace_text_in_files() {
    write_info "rename" "Replacing text in files from \"$PROJECT_NAME\" to \"$new_project_name\""
    find . -type f -exec sed -i '' "s/$PROJECT_NAME/$new_project_name/g" {} \;
    return 0
}

# Check if a new project name is provided as a command-line argument
if [ -z "$1" ]; then
    # Prompt the user for the new project name if no argument is given
    read -p "Enter the new project name: " new_project_name
else
    new_project_name=$1
fi

# Rename files, directories, and replace text in files
rename_files_and_directories
replace_text_in_files

echo "Renaming and text replacement complete!"
exit 0