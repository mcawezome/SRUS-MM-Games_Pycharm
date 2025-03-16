# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh():
   return 1


def ash(key):
   return key

```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?
> Deterministic
> They all take an input and map it deterministically to an output value
> Such that for any given input its hash can be calculated consistently
> Mapping
> Hash functions implement a mapping function h: X → Y 
> Most perform a dimension reduction in the process. (all but ash in your examples)
> Many-to-One transformation
> Which is a Many-to-One transformation - Multiple inputs to the same output.
> Defined domain and range
> Specified input and output ranges of values

1. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some research to answer this question 😱

> ssh is uniform, deterministic, efficient. It has as poor collision resistance as possible. Zero sensitivity to input changes. Completely insecure.
> sum_of_ascii_values is not uniform. It is deterministic. It is efficient. Collision resistance is not ideal. Sensitivity to input isn't great as small changes to input produce small changes in output. insecure (can be puzzled out easily).
> pearson table is uniform, deterministic, extremely efficent (lookups and XOR only). Collisions OK but suffer from birthday paradox. High sensitivity to inputs. Secure enough but can reverse with brute force.
> ```pseudocode
Builtin hash for str
for current in str
   multiply current by multiplier (start 1000003)
   Add unicode code point on current
   modulo 2^n (bit-size modification)
   XOR with str length
''''
> builtin hash is moderately uniform, deterministic if seeded (random start), O(n) efficient. Good collision resistance. Medium sensitivity to inputs. possibly reversible.
> SHA256 extremely high uniformity, strictly deterministic, Reasonably efficient, Amazingly collision resistant, Strong sensitivity to inputs. cryptographically secure.

1. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> 1. Deterministic - Without this property retrieval in hash tables simply will not work.
> The next two are linked and comparable and effect memory allocation. 
> Memory is an important factor as it is a limited resource and memory reallocation should be avoided if possible
> 2. Uniformity - Uniformity defines the distribution of values within a hash function. Ultimately defining collision resistance.
> 3. Collision Resistance - This effects memory allocation significantly. Also effects runtime.

1. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would pick Pearson's Hash. Due to its positive qualities across the categories.
> Python builtin hash would be great also but does not satisfy project task requirement to implement a hash function.
> SHA256 is specifically for security or checksum applications, not a lookup table in a small project.

1. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.
```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```
```import random```

> access the random python library for generating pseudo-random numbers.

```random.seed(42)```

> seed or start the random algorithm with a given integer (42) for deterministic output.

```# INCORRECT: pearson_table = [random.randint(0, 255) for _ in range(256)]```

> Initially seemed fine.
> The line is incorrect because the table will generate 256 randoms numbers but will not include all numbers 0-255
> So there will be duplicates and missing values.

```pearson_table = list(range(256))```

> create a list of integers 0-255 in order

```random.shuffle(pearson_table)```

> shuffle disorganises the list and puts the list in a random order

```def pearson_hash(key: str, size: int) -> int:```

> define a function called pearson_hash with inputs key(str) and size(int) which returns an int

```hash_ = 0```

> start the hash at 0, this will update after every character is hashed

```for char in key:```

> loop through each character in key(str) with a for loop

```hash_ = pearson_table[hash_ ^ ord(char)]```

> ord(char) retrieves the ascii integer value of a given character.
> ^ is XOR bitwise operation. The benefit of this operation is sensitivity of inputs.
> Two similar inputs produce quite different outputs for such a simple operation.
> So in summary: Access the nth element in the random pearson table where n is previous hash(hash_) XOR with ord value of the char.

```return hash_ % size```

> return an integer which is the remainder of hash_ divided by list size
> hash_ could be an arbitrarily large number so modulo operation keeps it within index range.

1. Write pseudocode of how you would store Players in PlayerLists in a hash map.
> Giving example of Open Addressing instead of Chaining - which was used in Assessment Exercise.
> Pseudocode has core elements glossing over certain method implementations
```pseudocode
class PlayerList:
    """
    Hash table implementation for PlayerList using open addressing with double hashing (hash probing).
    
    Open addressing handles collisions by probing for next available slot.
    Double hashing uses two hash functions to minimize clustering.
    Tombstones mark deleted entries. So find_slot does not halt for deletions. Maintains probe sequence.
    """
    # Constants
    EMPTY = 0
    OCCUPIED = 1
    TOMBSTONE = 2

    function initialize(capacity):
        table = array of (key=None, player=None, status=EMPTY) with size capacity
        
    function find_slot(key):
       # Table full handling (implementation omitted)
    
        start_position = Player.hash1(key) mod capacity
        step = Player.hash2(key) mod capacity
        if step == 0: step = 1 # sanitises infinite loop
        position = start_position
        first_tombstone = None
        
        # Probe until finding key, empty slot, (table must not be full checked above)
        for _ from 0 to capacity-1:
            if table[position].status == EMPTY:
                # Once empty slot is found, search ends. We return first empty slot even if it's a tombstone.
                if first_tombstone is not None:
                    return first_tombstone, False
                return position, False
                
            if table[position].status == TOMBSTONE and first_tombstone is None:
                first_tombstone = position
                
            if table[position].status == OCCUPIED and table[position].key == key:
                return position, True
                
            position = (pos + step) mod capacity
    
    function get(key):
        position, found = find_slot(key)
        if found:
            return table[position].player
        return None
        
    function put(key, player):
        # Resize if needed (implementation omitted)
        position, found = find_slot(key)
        table[position] = (key, player, OCCUPIED)
            
    function delete(key):
        position, found = find_slot(key)
        if found:
            table[position] = (None, None, TOMBSTONE)
            return True
        return False
            
    function resize(new_size):
        # Copy occupied entries to new table (implementation omitted)
```

## Reflection

1. What was the most challenging aspect of this task?

> The most challenging aspect was understanding how __setitem__, __getitem__ and __delitem__ are implemented.
> I had initially used the index as input for each of these methods.
> Later I realised I am mimicking a Dictionary data type.
> So I re-implemented the methods using key as input.
> The challenge of understanding dunder methods therefore was overcome.

1. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Use a dictionary to store all keys and values.
> Possibly making the entire PlayerHashMap a shell class for inbuilt dictionaries.
> This would make the implementation as efficient as reasonably possible in Python.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
