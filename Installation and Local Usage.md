## Installation and Local Usage

### Step 1: Clone and Change Directory

```
git clone https://github.com/shaniljasani/KinConnections.git
```

```
cd KinConnecctions
```

### Step 2: Add a `.env` File

Use the `.env_EXAMPLE` file template to create a `config.py` file. Add your `Database APIKEY` to the file.

### Step 3: Set up a Python Virtual Environment in Directory

Run the following command to create a python virtual environment.

```
python3 -m venv venv
```

This will create a folder called `venv` in the current directory which should be the root of this project's directory. `venv` stores all the virtual environment binary files.

### Step 4: Run the Virtual Environment

The following command will start up the virtual environment

```
source venv/bin/activate
```

### Step 5: Download Dependencies

```
pip install -r ./requirements.txt
```

### Step 6: Start the Server

```
python3 app.py
```
