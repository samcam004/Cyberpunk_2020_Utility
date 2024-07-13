import sqlite3 as sq
from weapons_info import weapons_array


def create_database():
    print("Create DB")

    # Connect to the database (or create it if it doesn't exist)
    conn = sq.connect("cyberpunk2020.db")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS BodyArmor (
            TypeOfArmor TEXT PRIMARY KEY,
            Covers TEXT NOT NULL,
            SP INTEGER NOT NULL,
            EV INTEGER NOT NULL,
            Cost TEXT NOT NULL
        )
        """
    )

    # Create the Weapons table if it doesn't exist
    # Company will become Forigen Key later on.
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Weapons (
            Category TEXT NOT NULL,
            Company TEXT NOT NULL,
            Name TEXT PRIMARY KEY,
            Type TEXT NOT NULL,
            WeaponAccuracy INTEGER NOT NULL,
            Concealability TEXT NOT NULL,
            Availability TEXT NOT NULL,
            Damage TEXT NOT NULL,
            Ammo TEXT NOT NULL,
            NumberOfShots INTEGER NOT NULL,
            ROF INTEGER NOT NULL,
            Reliability TEXT NOT NULL,
            Range TEXT NOT NULL,
            Cost TEXT NOT NULL,
            Description TEXT NULL
        )
        """
    )

    # Create the Gear table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Gear (
            Category TEXT NOT NULL,
            Name TEXT PRIMARY KEY,
            Cost TEXT NOT NULL,
            Description TEXT NULL
        )
        """
    )

    # Create the Cyberware table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Cyberware (
            Category TEXT NOT NULL,
            Name TEXT NOT NULL,
            Surgery TEXT NOT NULL,
            ID CODE PRIMARY KEY,
            Description TEXT NOT NULL,
            Details TEXT NOT NULL,
            Cost TEXT NOT NULL,
            HLoss TEXT NULL
        )
        """
    )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def fill_bodyarmor_table():

    conn = sq.connect("cyberpunk2020.db")
    cursor = conn.cursor()

    armor_array = [
        ["Cloth, leather√", "Arms, Torso, possibly legs", 0, 0, "Varies"],
        ["Heavy leather", "Arms, Torso, possibly legs", 4, 0, "50.00"],
        ["Kevlar T-Shirt, Vest√", "Torso", 10, 0, "90.00"],
        ["Steel helmet", "Head", 14, 0, "20.00"],
        ["Light Armor jacket√", "Torso, Arms", 14, 0, "150.00"],
        ["Med Armor jacked√", "Torso, Arms", 18, 1, "200.00"],
        ["Flack vest", "Torso", 20, 1, "200.00"],
        ["Flack pants", "Legs", 20, 1, "200.00"],
        ["Nylon helmet", "Head", 20, 0, "100.00"],
        ["Heavy Armor jacket√", "Torso, Arms", 20, 2, "250.00"],
        ["Door Gunner's vest", "Torso", 25, 3, "250.00"],
        ["MetalGear™", "Whole Body", 25, 2, "600.000"],
    ]

    # Insert the 2D array into the BodyArmor table
    for row in armor_array:
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO BodyArmor (TypeOfArmor, Covers, SP, EV, Cost) VALUES (?, ?, ?, ?, ?)",
                row,
            )
        except sq.IntegrityError as e:
            print(f"IntegrityError: {e} - for row: {row}")
        except sq.Error as e:
            print(f"SQLite error: {e} - for row: {row}")

    # Commit the changes
    conn.commit()


def fill_weapons_table():
    conn = sq.connect("cyberpunk2020.db")
    cursor = conn.cursor()

    # Insert the 2D array into the BodyArmor table
    for row in weapons_array:
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO Weapons (Category, Company, Name, Type, WeaponAccuracy, Concealability, Availability, Damage, Ammo, NumberOfShots, ROF, Reliability, Range, Cost, Description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                row,
            )
        except sq.IntegrityError as e:
            print(f"IntegrityError: {e} - for row: {row}")
        except sq.Error as e:
            print(f"SQLite error: {e} - for row: {row}")

    # Commit the changes
    conn.commit()


def fill_gear_table():
    """
    Category TEXT NOT NULL,
    Name TEXT PRIMARY KEY,
    Cost TEXT NOT NULL,
    Description TEXT NULL
    """


def main():
    print("Test")
    create_database()
    fill_bodyarmor_table()
    fill_weapons_table()


if __name__ == "__main__":
    main()
