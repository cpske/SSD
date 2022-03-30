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


## Structural Patterns

Structural Design Patterns are concerned with the definition of classes.

The Structural Patterns in the original GoF Patterns Book are:

| Pattern  | Intent |
|----------|--------|
| Adapter  | Adapt a class's interface to another interface that a client expects. |
| Bridge   | Decouple an abstraction from its implementation so that the two can vary independently. |
| Composite | Compose objects into collections so that clients can treat individual objects and composite objects the same. |
| Decorator | Add new responsibilities to a class or object, without modifying the original class's code. |
| Facade | Provide a unified interface to a set of interfaces in a subsystem. |
| Flyweight | Enable objects to be shared (reused) to reduce number of objects, by externalizing state. |
| Proxy | Provide a surrogate or placeholder for another object to control access to it. |

You have already seen Adapter, Composite, and Decorator many times.


