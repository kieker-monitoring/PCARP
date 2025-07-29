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

The following will walk you through the complete pipeline methodology. The data from the previous experiment is included with this package.
You can skip the following and run the pipeline from these logs if necessary.
Note: it is important to do the static analysis first, as to not skew the static analysis results with the added code for the dynamic analysis intrumentation.

### Static Analysis

From the root, run the static analyzer.
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

Install the instrumented app. This process varies from app to app. The following should work in most cases.
```
pip install <path/to/app> --no-build-isolation --no-compile --use-feature=fast-deps
```
Or

```
python3 -m build <path/to/app>
pip install <path/to/app>/dist/*.whl -v
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

## Running the pipeline

Now, run the pipeline.
```
./scripts/pipeline.sh /tmp/kieker* bin/static combined-helloWorld
```

