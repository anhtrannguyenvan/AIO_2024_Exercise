#Tự luận
#### Câu 1:
from collections import deque
def sliding_window(nums, k):
    if not nums:
        return []
# lưu chỉ số của các phần tử trong cửa sổ trượt
    deq = deque()
    result = []
    
    for i in range(len(nums)):
        # Loại bỏ các phần tử không thuộc cửa sổ trượt hiện tại
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        # Loại bỏ các phần tử từ cuối deque nếu chúng nhỏ hơn hoặc bằng phần tử hiện tại
        while deq and nums[deq[-1]] <= nums[i]:
            deq.pop()
        
        # Thêm chỉ số của phần tử hiện tại vào cuối deque
        deq.append(i)
        
        # Thêm phần tử lớn nhất của cửa sổ trượt hiện tại vào danh sách kết quả
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result

#check
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding_window(num_list, k))

#cau2:
def count_letters(word):
    letter_count = {}
    # Duyệt qua từng chữ cái trong từ
    for letter in word:
        # Chuyển chữ cái thành chữ thường để không phân biệt chữ hoa và chữ thường
        letter = letter.lower()
        
        # Kiểm tra xem chữ cái đã có trong dictionary chưa
        if letter in letter_count:
            # Nếu có rồi, tăng giá trị đếm lên 1
            letter_count[letter] += 1
        else:
            # Nếu chưa có, khởi tạo giá trị đếm là 1
            letter_count[letter] = 1
            
    return letter_count
#check
word ="AIOvn"
print(count_letters(word))

##Cau3:
import requests
def count_words_in_file(file_path):
    # Khởi tạo dictionary để đếm số lần xuất hiện của các từ
    word_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            # Chuyển tất cả các chữ cái thành chữ thường
            line = line.lower()
            # Tách các từ trong dòng
            words = line.split()
            # Đếm số lần xuất hiện của mỗi từ
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    return word_count

# Ví dụ sử dụng
file_path = '!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko' 
word_counts = count_words_in_file(file_path)
print(word_counts)


###TRAC NGHIEM
#cauhoi1:
def max_kernal(num_list, k):
    result = []
    
    deq = deque()
    result = []
    
    for i in range(len(num_list)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        while deq and num_list[deq[-1]] <= num_list[i]:
            deq.pop()
    
        deq.append(i)
        
        # Thêm phần tử lớn nhất của cửa sổ trượt hiện tại vào danh sách kết quả
        if i >= k - 1:
            result.append(num_list[deq[0]])
    
    return result
#Check 
assert max_kernal([3,4,5,1,-44],3) == [5,5,5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernal(num_list, k))

##Cauhoi2:
def character_count(word) :
    character_statistic = {}
    
    for letter in word:
        # Chuyển chữ cái thành chữ thường để không phân biệt chữ hoa và chữ thường
        letter = letter.lower()
        
        # Kiểm tra xem chữ cái đã có trong dictionary chưa
        if letter in character_statistic:
            # Nếu có rồi, tăng giá trị đếm lên 1
            character_statistic[letter] += 1
        else:
            # Nếu chưa có, khởi tạo giá trị đếm là 1
            character_statistic[letter] = 1
            
    return character_statistic
##Check result
assert character_count ("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}

print(character_count('smiles'))

##Cauhoi3:
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': id}, stream=True)
    response.raise_for_status()

    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            f.write(chunk)

def count_word(file_path):
    counter = {}
    
    # Mở và đọc nội dung file
    with open(file_path, 'r') as file:
        for line in file:
            # Chuyển tất cả các chữ cái thành chữ thường
            line = line.lower()
            # Tách các từ trong dòng
            words = line.split()
            # Đếm số lần xuất hiện của mỗi từ
            for word in words:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    
    return counter

# Tải file từ Google Drive
file_id = '1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
destination = 'P1_data.txt'
download_file_from_google_drive(file_id, destination)

# Kiểm tra hàm
file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])

##Cau4
def levenshtein_distance(token1, token2):
    # Khởi tạo ma trận để lưu khoảng cách Levenshtein
    m = len(token1)
    n = len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Trường hợp cơ sở khi một trong hai chuỗi rỗng
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Tính toán khoảng cách Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if token1[i - 1] == token2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,        # Xóa
                           dp[i][j - 1] + 1,        # Thêm
                           dp[i - 1][j - 1] + cost) # Thay thế hoặc giữ nguyên
    
    # Khoảng cách Levenshtein là giá trị ở ô dưới cùng bên phải
    return dp[m][n]

# Kiểm tra các trường hợp
assert levenshtein_distance("hi", " hello ") == 4
print(levenshtein_distance(" hola ", " hello "))

##Cauhoi5
def check_the_number(number):
    list_of_numbers = []
    
    # Append numbers from 1 to 4 into list_of_numbers
    for i in range(1, 5):
        list_of_numbers.append(i)
    
    if number in list_of_numbers:
        result = "True"
    else:
        result = "False"
    
    return result

# Testing the function with assertions and print statements
N = 7
assert check_the_number(N) == "False"

N = 2
result = check_the_number(N)
print(result)

#Cauhoi6:
def my_function(data, max_value, min_value):
    result = []
    for i in data:
        if i < min_value:
            result.append(min_value)
        elif i > max_value:
            result.append(max_value)
        else:
            result.append(i)
    return result

# Test cases
my_list = [5, 2, 5, 0, 1]
max_value = 1
min_value = 0
assert my_function(data=my_list, max_value=max_value, min_value=min_value) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
max_value = 2
min_value = 1
print(my_function(data=my_list, max_value=max_value, min_value=min_value))

#Cauhoi7:
def my_function_7(x, y):
    # Concatenate y to x using extend
    x.extend(y)
    return x

# Test cases
list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function_7(list_num1, my_function_7(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function_7(list_num1, my_function_7(list_num2, list_num3)))

##Cauhoi8
def my_function_8(n):
    # Sử dụng hàm min để tìm giá trị nhỏ nhất trong list n
    min_value = min(n)
    return min_value

# Test case 1
my_list = [1, 22, 93, -100]
assert my_function_8(my_list) == -100

# Test case 2
my_list = [1, 2, 3, -1]
print(my_function_8(my_list))

#Cauhoi9:
def my_function_9(n):
    # Sử dụng hàm max để tìm giá trị nhỏ nhất trong list n
    max_value = max(n)
    return max_value

# Test case 1
my_list = [1001 , 9 , 100 , 0]
assert my_function_9(my_list) == 1001

# Test case 2
my_list = [1 , 9 , 9 , 0]
print(my_function_9(my_list))

##Cauhoi10:
def my_function_10(integers, number=1):
    return any(item == number for item in integers)

# Test case 1
my_list = [1, 3, 9, 4]
assert my_function_10(my_list, -1) == False

# Test case 2
my_list = [1, 2, 3, 4]
print(my_function_10(my_list, 2))

#Cauhoi11
def my_function_11(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)

# Test case 1
assert my_function_11([4, 6, 8]) == 6

# Test case 2
print(my_function_11())

##Cauhoi12:
def my_function_12(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var

# Test case 1
assert my_function_12([3, 9, 4, 5]) == [3, 9]

# Test case 2
print(my_function_12([1, 2, 3, 5, 6]))

# Tu Ba Van Anh