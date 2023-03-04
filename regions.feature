Feature: The "Route Guide" webpage of mountainproject.com

 Scenario Outline: States are split into regions with at least one route each
   Given we have navigated to the "<state>" webpage from the route directory
   When  we look for the "<region>" on the webpage
   Then  we find that the region has at least one route

   Examples: Various regions in Ohio
    | state     | region         |
    | Ohio      | Central Ohio   |
    | Utah      | Southeast Utah |
    | Iowa      | Lake Delhi     |
    | New York  | Adirondacks    |
    | Kentucky  | Lexington      |
    | Maryland  | Locust Grove   |


   Scenario: The webpage has a list of the Top 10 Classic Rock Climbing Routes
     Given we are at the "Route Guide" webpage
     When  we check to see how many routes are on the Top 10 list
     Then  the list should contain exactly 10 routes
