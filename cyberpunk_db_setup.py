import sqlite3 as sq
from weapons_info import weapons_array
from armor_info import armor_array
from gear_info import gear_array

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
            Cost TEXT NOT NULL
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
    conn = sq.connect("cyberpunk2020.db")
    cursor = conn.cursor()

    print('Gear List')
    # Insert the 2D array into the BodyArmor table
    for row in gear_array:
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO Gear (Category, Name, Cost) VALUES (?, ?, ?)",
                row,
            )
        except sq.IntegrityError as e:
            print(f"IntegrityError: {e} - for row: {row}")
        except sq.Error as e:
            print(f"SQLite error: {e} - for row: {row}")

    # Commit the changes
    conn.commit()


def main():
    print("Test")
    create_database()
    fill_bodyarmor_table()
    fill_weapons_table()
    fill_gear_table()


if __name__ == "__main__":
    main()
