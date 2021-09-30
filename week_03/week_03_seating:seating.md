Design an algorithm that would seat people more equitably.

- Write up a description of your algorithm and save it as week_03_seating/seating.pdf. Make sure this description states how
  it should improve equity and also how it might affect other concerns.

- NO CODE NEEDED HERE just a description but make a note of implementation issues that might make your algorithm more practical or more difficult to implement

One way to approach the plane seating algorithm to make it more equitable is to eliminate the ability to purchase a specific seat and randomly assign everyone on the plane to a seat. However, this will lead to some people being randomly assigned a window when they didn't actually pay more for the better seat. Some people do prefer the aisle seat or even a middle seat if it guarantees them sitting next to their travel companion.

Perhaps there is a way for people to rank their choices: window, middle, aisle that can be factored into the algorithm. For example, I can list my preference order (aisle, window, middle) when I buy my ticket and the plane will do their best to honor everyone's selections by sorting people by least desired seat first (presumably people requesting middle seats). To complicate matters further, people could assign a percentage value to how desired their seat choices are. For example, I prefer aisle to window but not by much. I might rank them as such: aisle (45%), window (40%), middle (15%). This way the airline knows that they could put me in an aisle seat or a window seat and I would be pretty much content either way, but have almost no desire to be seated in a middle seat.

While this approach to seating may be more equitable because people get to state their preferences more explicitly, it will certainly complicate the code. For example, how to decide between two people who both want a window seat or aisle seat but only one of those seats is left? Does the algorithm randomly select one of the two people to occupy that seat? What if someone puts that they want a window seat (100%) and no other option? Perhaps only people who want the least desired middle seat should get first pick. There are a lot of ways to optimize this algorithm and not necessarily a "right" answer.
