class PlayerUID:
    """A descriptor that validates and manages a player's unique identifier (uid).

    The uid must be a string representing a positive integer. Leading zeros and
    whitespace are stripped during validation.
    """

    def __init__(self):
        """Initializes a new PlayerUID descriptor.

        The descriptor creates a unique attribute name for each instance.
        """
        self.name = f"_{id(self)}_uid"

    def __get__(self, instance, owner):
        """Gets the player's unique identifier.

        Args:
            instance: The Player instance.
            owner: The Player class.

        Returns:
            str: The player's UID, or None if not set.
        """
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        """Sets the player's unique identifier.

        Args:
            instance: The Player instance.
            value: The UID value to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value cannot be converted to a positive integer.
        """
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
        """Deletes the player's unique identifier.

        Args:
            instance: The Player instance.

        Raises:
            AttributeError: Player UID cannot be deleted.
        """
        raise AttributeError("Cannot delete player UID")


class PlayerName:
    """Descriptor for player unique name.

    Helps to validate name is a str without whitespace.

    Attributes:
        name: Internal attribute name for storing the player name.
    """

    def __init__(self):
        """Initializes the PlayerName descriptor.

        The descriptor creates a unique attribute name for storing player names.
        """
        self.name = f"_{id(self)}_name"

    def __get__(self, instance, owner):
        """Gets the player's name.

        Args:
            instance: The Player instance.
            owner: The Player class.

        Returns:
            str: The player's name, or None if not set.
        """
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        """Sets the player's name.

        Args:
            instance: The Player instance.
            value: The name to set.

        Raises:
            ValueError: If name is not a non-empty string.
        """
        # Validate name is a non-empty string
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Player name must be a non-empty string")
        # Store sanitized name (stripped of extra whitespace)
        setattr(instance, self.name, value.strip())

    def __delete__(self, instance):
        """Deletes the player's name.

        Args:
            instance: The Player instance.
        """
        # Reset to default name when deleted
        setattr(instance, self.name, "Anonymous")


class Player:
    """A class representing a player.

    Attributes:
        uid (str): Unique identifier for the player.
        name (str): Display name of the player.
    """
    # Define descriptors for attributes
    uid = PlayerUID()
    name = PlayerName()

    def __init__(self, uid: str, name: str) -> None:
        """Initializes a new Player instance.

        Args:
            uid: Unique identifier for the player.
            name: Display name of the player.
        """
        self.uid = uid
        self.name = name

    def __repr__(self):
        """Returns the string representation of the Player instance.

        Returns:
            str: A string in the format "Player(uid='<uid>', name='<name>')".
        """
        # No need for __str__ as __repr__ is clear and concise
        return f"Player(uid='{self.uid}', name='{self.name}')"
