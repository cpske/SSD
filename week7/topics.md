## Descriptor Classes (Chapter 10)

In Domain modeling, Larman refers to "*Description Classes*" or "*Specification Classes*".
- What are they?
- Why (and when) to use them in a domain model? 

- When (page 142 of Larman 2E)
  - we need a description about an item or service independent of the current existance or any instances of the item or service
  - deleting all instances would result in a loss of information that needs to be maintained
  - it reduces redundant or duplicated information


Examples:

- A LineItem represents the purchase of some quantity of a Product.    
  The specification class is Product, or ProductSpecification or ProductDescriptor.

- Students at KU enroll in what?  A Course? (no!)    

  - Students enroll in an OfferedCourse or CourseSection
  - CourseSection refers to a Course and
    - year & semester
    - section number
    - instructor
    - meeting time and location
    - exam code
  - Course (or CourseDescription) is something in the university catalog. It has
    - course id
    - a description
    - credits
    - prerequisites
    - department that provides it

- What represents a student enrollment in a course?


- An Airline Flight.  What is the flight descriptor? What is the flight instance?

  - For example, Delta Airlines flight 1 from Tokyo to Los Angeles, every day


## Chapter 11: Adding Associations in Domain Models

What info can you show on an association?

- role name
- role multiplicity
- role direction (navigability)
- (middle of line) verb-phrase description of the relationship

Example: NextGen POS model, Figure 11.8 on page 164

## Chapter 12: Adding Attributes

When to show something as...
* an attribute
* an association to another object?

Larman's view: p. 168 "Keep Attributes Simple"


