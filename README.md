```python
# Setup
from s1db import S1
api = S1("token-here")

# Set Object:
api.set('key', {'foo': 'bar'}

# Set Raw:
api.set_raw('key', 'Raw Data')

# Get Object:
api.get('key')

# Get Raw:
api.get_raw('key')

# Delete 
api.delete('key')

# Get All Keys -> Returns Object:
api.get_keys()
```