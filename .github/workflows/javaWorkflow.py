name: Java Workflow

on:
  push:
    branches:
      - main  # Replace 'main' with the branch name you want to trigger the workflow on

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Java
      uses: actions/setup-java@v1
      with:
        java-version: '8'  # Java 8

    - name: Build and run Java code
      run: |
        javac ./.github/workflows/Hello.java  # Compile the Java code
        java -cp ./.github/workflows/Hello.java  # Replace 'your_class_file_name' with the name of the compiled class file
