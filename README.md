# S1 Python

A barebones key-value store that requires no setup besides a token. This is the Python Library for S1. Find more information [here](https://github.com/Kognise/S1)

## Getting A Token

Head over to [s1.kognise.dev/token](https://s1.kognise.dev/token) to get a token. Don't share this with anyone as it's your key to accessing all your data on your S1 DB. You can store this as an environment variable. 

## Installation

First, install S1 with `pip`:
```bash
$ pip install s1db
```

Then you can import it like so:
```python
from s1db import S1

# Replace "your-token-here" with the token you got from the URL above.
api = S1("your-token-here")
```

## Usage

**Setting Objects as Values:**

To set a Python object as a value use the `S1.set()` method.
```python
api.set('keyname', 123)
api.set('keyname0', [23])
api.set('keyname1', {'foo': 'bar'})
```

The set method will automatically serialize your data for you into valid JSON to be stored on the S1 DB.

**Getting An Object:**

To get an object from your S1 DB use the `S1.get()` method.

```python
api.get('keyname') # Returns: 123 based on the set example from above.
api.get('keyname0') # Returns: [23] as a list based on the set example from above.
api.get('keyname1') # Returns: {'foo': 'bar'} as a Python dict based on the set example from above.
```

**Setting Raw Values:**

To set a raw string as a value use the `S1.set_raw()` method.

```python
api.set_raw('keyname-raw', '12')
api.set_raw('keyname-raw0, '{"foo": "bar"}')
```

The set_raw method does not do any JSON serialization and raw items cannot be returned with the `get()` method.

**Getting Raw Values:**

To get a raw value from a key use the `S1.get_raw()` method.

```python
api.get_raw('keyname-raw') # Returns: 12 with no serialization
api.get_raw('ketname-raw0') # Returns: '{"foo": "bar"}' as string
```

**Deleting Keys:**

To delete data use the `S1.delete()` method.

```python
api.delete('keyname')
```

**Getting All Keys:**

To get all your keys use the `S1.get_keys()` method.

```python
api.get_keys() # Returns: List of key names as Python object.
```
