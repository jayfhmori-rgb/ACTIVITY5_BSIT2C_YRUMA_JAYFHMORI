from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def choose_structure():
    print("\n=== SELECT DATA STRUCTURE ===")
    print("1. Array Stack")
    print("2. Linked Stack")
    print("3. Circular Array Queue")
    print("4. Linked Queue")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        capacity = int(input("Enter stack capacity: "))
        return ArrayStack(capacity), "stack"
    if choice == "2":
        return LinkedStack(), "stack"
    if choice == "3":
        capacity = int(input("Enter queue capacity: "))
        return ArrayQueue(capacity), "queue"
    if choice == "4":
        return LinkedQueue(), "queue"

    print("Invalid choice.")
    return None, None


def run_structure(structure, kind):
    while True:
        print("\n=== OPERATIONS ===")
        if kind == "stack":
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek Front")

        print("4. Check if Empty")
        if hasattr(structure, "is_full"):
            print("5. Check if Full")
        print("6. Display")
        print("0. Return to Main Menu")

        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                value = input("Enter value: ")
                if kind == "stack":
                    structure.push(value)
                    print("Value pushed successfully.")
                else:
                    structure.enqueue(value)
                    print("Value enqueued successfully.")
            elif choice == "2":
                print("Popped:" if kind == "stack" else "Dequeued:",
                      structure.pop() if kind == "stack" else structure.dequeue())
            elif choice == "3":
                print("Top:" if kind == "stack" else "Front:",
                      structure.peek() if kind == "stack" else structure.peek_front())
            elif choice == "4":
                print("Empty:", structure.is_empty())
            elif choice == "5" and hasattr(structure, "is_full"):
                print("Full:", structure.is_full())
            elif choice == "6":
                print("Current structure:", structure.display())
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def check_parentheses():
    expression = input("Enter an expression: ")
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack[-1] != pairs[character]:
                print("Parentheses are NOT balanced.")
                return
            stack.pop()

    if stack:
        print("Parentheses are NOT balanced.")
    else:
        print("Parentheses are balanced.")


def simulate_print_queue():
    queue = LinkedQueue()
    while True:
        print("\n=== PRINT QUEUE ===")
        print("1. Add print job")
        print("2. Print next job")
        print("3. Show waiting jobs")
        print("0. Return to Main Menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            job_id = input("Enter job ID: ").strip()
            try:
                pages = int(input("Enter number of pages: "))
                if pages <= 0:
                    print("Pages must be greater than zero.")
                    continue
            except ValueError:
                print("Please enter a whole number for pages.")
                continue
            queue.enqueue({"id": job_id, "pages": pages})
            print("Print job added.")
        elif choice == "2":
            try:
                job = queue.dequeue()
                print("Printing job:", job["id"])
                print("Pages:", job["pages"])
                print("Print job completed.")
            except IndexError as error:
                print("Error:", error)
        elif choice == "3":
            jobs = queue.display()
            if not jobs:
                print("No jobs waiting.")
            else:
                print("Waiting jobs:")
                for job in jobs:
                    print("Job ID:", job["id"], "| Pages:", job["pages"])
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n================================")
        print(" STACKS AND QUEUES PROGRAM")
        print("================================")
        print("1. Use a Data Structure")
        print("2. Check Balanced Parentheses")
        print("3. Simulate a Print Queue")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                structure, kind = choose_structure()
                if structure is not None:
                    run_structure(structure, kind)
            elif choice == "2":
                check_parentheses()
            elif choice == "3":
                simulate_print_queue()
            elif choice == "0":
                print("Program terminated.")
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print("Input error:", error)


if __name__ == "__main__":
    main()
