# CoPlane-Interview

Repository structure:
- practice_`<number>`: folder with practice code...
- interview: folder used in the interview

## What is a rule engine?

A rule engine uses rules, which are conditional statements, to evaluate inputs. By having rules in a yaml file we can more easily maintain the code for the engine and better scale to use different rules for different purposes (the engine just consumes the rules).

### Practice

#### practice_1

#### practice_2

#### practice_3

#### practice_4

rules engine from pycon...

### Useful links and Libs..

- Discussion: https://stackoverflow.com/questions/53421492/python-rule-based-engine
- clipspy: https://clipspy.readthedocs.io/en/latest/
  - https://pypi.org/project/clipspy/
- rule-engine: https://pypi.org/project/rule-engine/
- durable_rules: https://github.com/jruizgit/rules
- pyke: http://pyke.sourceforge.net/index.html
- pyknow: https://github.com/buguroo/pyknow
- intellect: https://github.com/nemonik/Intellect
- business-rules: https://github.com/venmo/business-rules
- drools: https://www.drools.org/

### Videos...

Simple example with and without clipspy: https://www.youtube.com/watch?v=0HQSCXU-8NA

#### PyCon Sweden
PyCon Sweden: https://www.youtube.com/watch?v=Lsi1ZhmbNDc

Rules Rule - practice_4

https://martinfowler.com/bliki/RulesEngine.html

https://pypi.org/project/funnel-rules-engine/

https://github.com/funnel-io/funnel-rules-engine

## Durable Execution Engine

practice_5

## Two way sync

maintaining data consistency and enabling seamless collaboration between different platforms. defining sync rules, mapping fields, automating updates, and ensuring secure, real-time data exchange between the platforms

https://exalate.com/blog/two-way-integration/

id, created_at, first_entry_id, updated_at
1,11111110,1
2,11111112,2
3,11111116,3
4,11111117,1
5,11111118,5
6,11111119,6


a distributor to push to 3 party
a "monitoring" to pull data from the 3 party in a set interval - how can we query the 3 party? what are the options we have?
GET data FROM users WHERE updated=(from last_pool_time to now)

last_pool_time we keep in our own side to know when was the time of the last successful data pull.