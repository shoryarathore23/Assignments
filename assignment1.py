# ==========================================
# DICTIONARY OPERATIONS
# ==========================================
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
print("Initial Dictionary:", student_scores)

student_scores['David'] = 92       
removed_score = student_scores.pop('Bob')   
all_keys = student_scores.keys()     
all_values = student_scores.values()   
specific_score = student_scores.get('Charlie')  

print("Updated Dictionary:", student_scores)
print("Dictionary Keys:", list(all_keys))
print("Dictionary Values:", list(all_values))
print("-" * 40)


# ==========================================
# TUPLE OPERATIONS
# ==========================================
numbers_tuple = (15, 25, 25, 35, 45)
print("Base Tuple:", numbers_tuple)

count_25 = numbers_tuple.count(25)  
index_35 = numbers_tuple.index(35)  
tuple_len = len(numbers_tuple)    
max_val = max(numbers_tuple)     
min_val = min(numbers_tuple)   

print("Count of 25:", count_25)
print("Index of 35:", index_35)
print("Tuple Length:", tuple_len)
print("Maximum Element:", max_val)
print("Minimum Element:", min_val)
print("-" * 40)


# ==========================================
# LIST OPERATIONS
# ==========================================
my_items = [12, 3, 7]
print("Starting List:", my_items)

my_items.append(6)      
my_items.insert(2, 10)   
my_items.remove(3)      
popped_val = my_items.pop()      
my_items.sort()         

print("Sorted Final List:", my_items)