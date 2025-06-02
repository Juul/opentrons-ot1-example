
This is a work in progress example app for the OpenTrons OT1 liquid handling robot with instructions for how to get it working on modern Linux. Tested on Debian 12.9.0 Bookworm.

WORK IN PROGRESS, NOT YET TESTED!

# Setup

```
virtualenv myenv
source myenv/bin/activate

pip install opentrons==2.5.2
```

A static copy of `myenv/lib` is included in `opentrons_lib.tar.gz` in case any of the dependencies disappear from the interwebs.

To get this to work on modern python 3 you need to apply a fix to the opentrons library:

```
cp fixes/trace.py myenv/lib/python3.11/site-packages/opentrons/util/
```

# Running

If you haven't already, then run `source myenv/bin/activate` then:

```
./main.py
```

To actually run this on your robot edit the `robot.connect()` call to e.g. `robot.connect("/dev/ttyUSB0")` or whatever your serial device is.

# API documentation

I printed the API docs from https://docs.opentrons.com/o1/ to PDF and saved them in `api_docs/` in case they disappear.

Note that the official docs mention the `robot.simulate()` function but that disappeared in version 2.5.0 . I think the equivalent might be to do `robot.connect('Virtual Smoothie')` but not sure. If you need it then version 2.4.2 has it which is included in `old_versions/`.


