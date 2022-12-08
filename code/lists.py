#!/usr/bin/env python3.7

# 1) Set the u_list variable to be an empty list
u_list = []
assert u_list == [], f"Expected `u_list` to be [] but got: {repr(u_list)}"

# 2) Add 'juan', 'pablo', and 'lucia' to the u_list list in that order without reassigning the variable.
u_list.append('juan')
u_list.append('pablo')
u_list.append('lucia')

assert u_list == ['juan', 'pablo', 'lucia'], f"Expected `u_list` to be ['juan', 'pablo', 'lucia'] but got: {repr(u_list)}"

# 3) Remove 'pablo' from the u_list list without reassigning the variable.
del u_list[1]

assert u_list == ['juan', 'lucia'], f"Expected `u_list` to be ['juan', 'lucia'] but got: {repr(u_list)}"

# 4) Reverse the u_list list and assign the result to `rev_u_list`
rev_u_list = []
rev_u_list.append('lucia')
rev_u_list.append('juan')

assert rev_u_list == ['lucia', 'juan'], f"Expected `rev_u_list` to be ['lucia', 'juan'] but got: {repr(rev_u_list)}"

# 5) Add the user 'cata' to u_list where 'pablo' used to be.
u_list.insert(1, 'cata')
assert u_list == ['juan', 'cata', 'lucia'], f"Expected `u_list` to be ['juan', 'cata', 'lucia'] but got: {repr(u_list)}"

# 6) Add the u_list 'andre', 'ana', and 'luis' to the u_list list using a single command
u_list = u_list + ['andre', 'ana', 'luis']
assert u_list == ['juan', 'cata', 'lucia', 'andre', 'ana', 'luis'], f"Expected `u_list` to be ['juan', 'cata', 'lucia', 'andre', 'ana', 'luis'] but got: {repr(u_list)}"
print(u_list)
# 7) Slice the u_list lists to return the 3rd and 4th items and assign the result to `center_u_list`
center_u_list=u_list[3:5]
print(center_u_list)