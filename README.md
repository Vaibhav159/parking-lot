# Parking-lot Problem

## Problem Statement

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:-

1. We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
2. And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

Due to government regulation, the system should provide us with the ability to find out:-

- Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
- Slot number in which a car with a given vehicle registration plate is parked.
- Slot numbers of all slots where cars of drivers of a particular age are parked.

We interact with the system via a file-based input system, i.e. it should accept a filename as an input. The file referenced by filename will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.

## Running the Code

Installation of Python.

```bash
sudo apt install python3.8
```

```python
python3 allocation.py <inputs/input.txt> outputs/output.txt
python3 allocation.py <inputs/input1.txt> outputs/output1.txt
python3 allocation.py <inputs/input2.txt> outputs/output2.txt
```

## Assumptions

1. There'll be only one Create_parking_lot in complete test file and it'll be at the beginning of the file?
2. All cars will have a distinct unique registration number.
3. Commands will be always in right format.
4. Valid age will be provided.

## Edge Cases :

1. If Slot number is greater than capacity or less than 1, output would be "Slot number {slot_number} does not exist".
2. If Invalid command is provided, program will break from the execution.
3. If Parking is full, output for future park commands will be 'Parking Full, Car with vehicle registration number "{vehicle_number}" cant be parked'.
4. While searching for drivers with age or vehicle number, if no cars are found, output would be "Driver / Vehicle Not Found".
5. If leave slot_number is vacant, output will be “Slot already vacant”.

## Note:

Last Line of the input https://gist.github.com/tarungarg546/6200f936f2208bad5d9d0e053d773489 gives "Vehicle Not Found" in comparsion to ""(empty) line is sample output.

### Author

Vaibhav Lodha
