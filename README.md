# Static and Dynamic Analysis of Python Software replication-package

This is the replication package for the following paper:
Static and Dynamic Analysis of Python Software

## Authors

Daphné Larrivain
<daphne.larrivain@ecole.ensicaen.fr>
ENSICAEN, Caen, France

Shinhyung Yang
<shinhyung.yang@email.uni-kiel.de>
Kiel University, Kiel, Germany

Wilhelm Hasselbring
<hasselbring@email.uni-kiel.de>
Kiel University, Kiel, Germany

## Replication

This section guides you through the full pipeline methodology.  
All necessary data from the previous experiment is bundled with this package, so you can skip the data collection phase and run the pipeline directly using the provided logs.

---

> **Note:**
> It is important to perform **static analysis first**.
> Running dynamic instrumentation beforehand may introduce additional code that could skew the static analysis results.

## Recommended Development Environment

To ensure consistency and avoid setup issues, **we strongly recommend using the provided virtual machine**.

- The project has already been cloned to:  
  `~/Desktop/PCARP`
- All required dependencies and configurations are pre-installed.
- VM password: `osboxes.org`

You're ready to start working immediately—no additional setup required!

## Prerequisites for Local Development

If you choose to work from your own environment rather than a containerized or preconfigured setup, ensure the following tools and dependencies are installed:

## Core Tools

- **Git**
- **Python 3.13**  
  _Pro tip:_ Install via `ppa:deadsnakes` and configure it as an update-alternative alongside your system Python.
- **Pip**
- **Make**
- **JDK 17+**
- **Maven 3.9+**  
  _Tested with Maven versions 3.9.9 and 3.9.11._
- **Meson 0.63.3+**

## Python Dependencies

- Additional Python modules may be required depending on the application.  
  _Please refer to each app’s `requirements.txt` or documentation for details._

## Tulip Framework

- The **Tulip framework** is required.  
  _Pro tip:_ Since the `tulipgui` package has been discontinued, you’ll need to download a full Tulip build and unzip it. The GUI package is still bundled inside—just reference it via your `PYTHONPATH`.

---

> **Note:** This setup has been tested on **Ubuntu Jammy (22.04)**. Compatibility with other distributions may vary.

### Static Analysis

If you're working from the provided virtual machine, please **switch to the system Python** for this step.

The static analyzer includes an option to dynamically inspect installed dependencies. However, since **not all packages are yet compatible with Python 3.13**, it's recommended to:

- **Temporarily switch to an earlier Python version** (e.g., Python 3.10), or  
- **Avoid using the `-e` option** with the analyzer.

To switch Python versions on Ubuntu:

```
sudo update-alternatives --config python3
python3 --version  # Confirm the active version
```

Then From the root of the replication package, run the static analyzer.
```
time python3 tools/pyparse/src/pyparse/pyparse.py \
 -i <app_dir> \
 -o <static_out_dir> \
 -m both -e
```

### Dynamic analysis

Build and install the Otkt utilities (collector and python module).
```
cd otkt-gen
make
cd ..
```

Instrument the target app. 
```
python3 <path/to/root>/tools/Otkt-Instrument/instrument -i <path/to/app>
```

Install the instrumented app. This process varies from app to app and touch ups may be required, hence the necessity to install these modules in development mode.
The latter allows for the changes made in the source files to be reflected in the installed version.
```
pip install -e <path/to/app> --no-build-isolation --no-compile --use-feature=fast-deps
```

Launch the collector.
```
cd otkt-gen
make run
```

From another terminal, run the entrypoint.
```
python3 python/UXsim-test.py
```
The collector can be stopped. Kieker logs have been created in `/tmp`.

## Running the Pipeline

To execute the pipeline, make sure you're using **Python 3.13**.  
This is essential because the `ggvis` tool relies on **Tulip Framework v6**, which is compatible only with Python 3.13.

Run the pipeline script as follows:
```
./scripts/pipeline.sh <dynamic-logs> <static-logs> <analysis-name>
```
- `<dynamic-logs>` : Path to dynamic analysis logs
- `<static-logs>` : Path to static analysis logs
- `<analysis-name>` : Custom name for the output directory

Once complete, you can view the generated graph at:
`<analysis-name>/mvis_combined/output.pdf`
