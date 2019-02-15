# NI Package Assembler

This project is designed to script the creation and handling of NI Packages
before they are zipped into their final form. This makes it simple for CI 
servers to build packages and set important details like version, 
dependencies and programmatic setting of package names.

### Information about NI Packages

NI Packages are basically self-extracting archives. You setup a directory on 
your computer in a specific way, as described 
[here](http://www.ni.com/documentation/en/ni-package-manager/18.5/manual/assemble-file-package/), 
and then call the nipkg binary to compress those files into a neat, 
versioned, "package". You can then use the NIPM client to extract that package 
on to a target computer.

For consistent terminology, we first break that process up into three parts:
  1. Assemble
  2. Compress
  3. Extract

The nipkg binary from National Instruments does a great job at steps two and 
three, but step one is manual. That is where this tool comes in.

## Installation

You will need NIPM from National Instruments and you need to add the nipkg.exe 
directory to your PATH variable. NIPM only works for Windows.
As of right now, this project uses Python 3.6. Install python, create a  
virtual environment and pip install the requirements.txt.

Activate your virtual environment and then install requirements.txt like this: 
```commandline
pip install -r requirements.txt
```

## Usage

The virtual environment you created above must be activated to use the tool.

**NOTE**
```
To simplify multiple calls to the same package, all of these functions 
will first look for an environment variable called `PKG_ROOT_DIRECTORY`. If 
this environment variable is not set, you need to pass the -d argument to 
every call. Usage of the -d argument OVERRIDES the environment variable.
```

### Create a default directory

If you don't already have a directory created, you can use this command to 
create a default package.
```commandline
python create_default_package.py [-d path/to/desired/root/folder/]
```
You will now see the default package folder created at the path specified by 
the PKG_ROOT_DIRECTORY environment variable, or passed into the -d argument.

This default directory is defined in this repo, feel 
free to change it to meet your needs.

### Add entire folders to your default package

Once you have a default directory, one of the most common things you need to 
do is add folders (usually outputs from various compilers) to specific 
installation target locations.
```commandline
python add_directory_to_package.py -i folder/to/copy -t <Installation Target>
```

This command uses the installation targets defined under "Name in File Package" 
[here](http://www.ni.com/documentation/en/ni-package-manager/18.5/manual/installation-target-roots/) 
e.g. "ProgramData"

### Changing the control file

After you've added all your folders and files, the last thing is to update the 
control file. This file is documented by NI,
[here](http://www.ni.com/documentation/en/ni-package-manager/18.5/manual/control-file-attributes/). 

```commandline
python update_control_file.py -a <Attribute name> -v <Attribute value>
```

The existing value of the attribute can be referenced using %ATTRIBUTE% 
in your value. e.g. `dev-%PACKAGE%` will set the Package attribute to what it 
`dev-` plus what it was before.
