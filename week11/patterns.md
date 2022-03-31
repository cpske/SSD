---
title: Identify Pattern Participants
---

### Instructions

Complete the table in the Google Doc template for this assignment.


### 1. Tkinter Event Handlers

Event handlers for GUI components use the *Observer Pattern*.
Consider this Python example:
```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

button = tk.Button(root, text="Press Me")
button.bind("<Button-1>", controller.handle_press)


class Controller:
    def handle_press(self, event):
        # show a pop-up dialog box (like Swing JOptionPane)
        messagebox.showinfo("OK", "Ouch. Don't press so hard!")    
```
In tkinter, events are named as strings.  `<Button-1>` means the 
left button press event.

Complete the table for how this example uses the Observer pattern.


### 2. Sorting a Collection

In Java, to sort a Collection use `java.util.Collections.sort`.
The `sort` method is overloaded. In this example, we will use the `sort`
method that accepts a `Comparator` parameter, which defines how to compare 
(order) two objects.  This is the most flexible way to sort things.

```java
Collections.sort( list, comparator);  // sorts a list in place
```

`Comparator` is an interface with a single method:
```java
interface Comparator<T> {  // T = type of objects being compared

     public int compare(T object1, T object2);
}
```
The **compare** method should return:

- -1 (any negative value) if object1 should come before object2 (`object1 < object2`)
-  0 if both objects have the same sort order
- +1 (any positive value) if object1 should come after object2 (`object1 > object2`)

Example:    
We want to sort some strings by **length**, so we define this comparator:

```java
class LengthComparator implements Comparator<String> {

    public int compare(String s1, String s2) {
        return s1.length() - s2.length();
    }
}
```

This example code reads a list of words, sorts them by length, and prints them:

```java
// Read a list of words from a file or other data source
// code for readWords is not shown.
List<String> words = readWords(); // returns a list of words

Comparator<String> compByLength = new LengthComparator();
Collections.sort(words, compByLength);

// print them
words.stream().forEach(System.out::println);
```

For shorter code, you can write the comparator as a *Lambda expression*
instead of defining a class that implements Comparator:

```java
Comparator<String> compByLength = (s1,s2) -> s1.length() - s2.length();
```

Complete the pattern table for this example.


### 3. Structural Design Patterns

Complete the table of structural patterns.

Note: some web sites have very *poor* descriptions of design patterns.
These sites have poor description and I suggest you avoid them: "geekforgeeks.org", "tutspoint.com".

Another structural pattern that is useful to know is the *Bridge Pattern*.

### 4. Improve Code by Applying a Pattern

This code gets petrol fuel prices for Thailand from a web service.
The "main" block prints the prices on the console.

<https://github.com/jbrucker/fuelprice>

The fuel prices can change at most once per day (at the start of the day),
so its inefficient to repeatedly call the web service every time the
code is run.

- Describe in words how to improve the code.  What pattern would you use?

- We don't want to make this code more complex. How would you implement your improvements without adding new code?  Include a UML class diagram of your idea (paste the image into your Google Doc).

- Are there any minor structural changes you would make to the `FuelPrice` class to make it easier to apply the pattern?

