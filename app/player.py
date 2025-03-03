class PlayerUID:
    """
    Descriptor for player unique identifier (uid)
    Helps to validate uid is always a positive number string.
    """

    def __init__(self):
        self.name = f"_{id(self)}_uid"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if isinstance(value, str):
            # No uid should have trailing or leading whitespace.
            value = value.strip()
            # Try to convert string to integer
            try:
                int_value = int(value)
            except ValueError:
                raise ValueError("Player UID must be a string convertible to a positive integer")
        else:
            raise TypeError("Player UID must be a string.")

        # Validate uid is a positive integer
        if int_value <= 0:
            raise ValueError("Player UID must be a positive integer")

        # if valid set to str version of the integer (removes leading 0's)
        setattr(instance, self.name, str(int_value))

    def __delete__(self, instance):
        raise AttributeError("Cannot delete player UID")


class PlayerName:
    """
    Descriptor for player unique name
    Helps to validate name is a str without whitespace.
    """

    def __init__(self):
        self.name = f"_{id(self)}_name"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        # Validate name is a non-empty string
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Player name must be a non-empty string")
        # Store sanitized name (stripped of extra whitespace)
        setattr(instance, self.name, value.strip())

    def __delete__(self, instance):
        # Reset to default name when deleted
        setattr(instance, self.name, "Anonymous")


class Player:
    """
    Player class (used later in PlayerList)
    """
    # Define descriptors for attributes
    uid = PlayerUID()
    name = PlayerName()

    def __init__(self, uid: str, name: str) -> None:
        self.uid = uid
        self.name = name

    def __repr__(self):
        return f"Player(uid='{self.uid}', name='{self.name}')"

    def __str__(self):
        return f"Player (uid={self.uid} named {self.name})"