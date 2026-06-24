class Student:
    def __init__(self, id, name, theory_score, practice_score, assignment_score):
        self.id = id
        self.name = name
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.assignment_score = assignment_score
        self.average_score = 0.0
        self.academic_type = ""
        self.calculate_average()
        self.classify_academic()
        
    def calculate_average(self):
        self.average_score = self.theory_score*0.4 + self.practice_score*0.4 +self.assignment_score*0.2
        self.average_score = round (self.average_score, 2)
    
    def classify_academic(self):
        if self.average_score < 5.0:
            self.academic_type = "Yếu"
        elif self.average_score < 6.5:
            self.academic_type = "Yếu"
        elif self.average_score < 8.0:
            self.academic_type = "Khá"
        else:
            self.academic_type = "Giỏi"
            
    def update_score (self, theory_score, practice_score, assignment_score):
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.assignment_score = assignment_score
        self.calculate_average()
        self.classify_academic()

header =  f"{'Mã sinh viên':<13} | {'Họ tên':<18} | {'Điểm lý thuyết':<15} | {'Điểm thực hành':<15} | {'Điểm bài tập':<15} | {'Điểm tổng kết':<15} | {'Học lực':<10}"  
class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_students (self, student):
        self.students.append(student)
        
    def print_table_header (self):

        print ("-"*len(header))
        print (header)
        print ("-"*len(header))
        
    def print_student_row (self, student):
        print (f"{student.id:<13} | {student.name:<18} | {student.theory_score:<15.2f} | {student.practice_score:<15.2f} | {student.assignment_score:<15.2f} | {student.average_score:<15.2f} | {student.academic_type:<10}")
        print ("-"*len(header))
    def show_all(self):
        if not self.students:
            print ("Không có sinh viên nào trong danh sách")
            return
        self.print_table_header()
        for s in self.students:
            self.print_student_row(s)
    
    def update_student (self, id, theory_score, practice_score, assignment_score):
        for s in self.students:
            if id == s.id:
                s.update_score(theory_score, practice_score, assignment_score)
                return True
        return False
    
    def delete_student (self, id):
        for s in self.students:
            if id == s.id:
                self.students.remove(s)
                return True
        return False

    def search_student (self, name):
        results = [s for s in self.students if name.lower() in s.name.lower()]
        if not results:
            print (f"Không tìm thấy sinh viên phù hợp. Có tên {name}")
            return
        self.print_table_header()
        for s in results:
            self.print_student_row(s)
            
    def is_id_exists (self, id):
        for s in self.students:
            if id == s.id.upper():
                return True
        return False
    
def get_non_empty_string (prompt):
    while True:
        value = input (prompt)
        if not value:
            print ("Không được để trống")
            continue
        return value
        
def get_valid_score (prompt):
    while True:
        try:
            score = float (input (prompt))
            if score >=0 and score <= 10:
                return score
            print ("Điểm lỗi")
        except ValueError:
            print ("Định dạng số không hợp lệ")            

def main ():
    Manager = StudentManager()
    Manager.add_students(Student("PTIT001", "Nguyễn Văn A", 5.0, 5.0, 5.0))
    Manager.add_students(Student("PTIT002", "Hoàng Dương B", 9.0, 9.0, 9.0)) 
    Manager.add_students(Student("PTIT003", "Trần Thị C", 8.0, 7.0, 7.0))   
    while True:
        print ("""
============ MENU ============
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật điểm sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Thoát""")
        choice = input ("Nhập vào lựa chọn của bạn: ")
        match choice:
            case "1":
                Manager.show_all()
            case "2":
                print ("============ Thêm sinh viên mới ============")
                id = get_non_empty_string("Nhập vào mã sinh viên cần thêm: ").upper().strip()
                if Manager.is_id_exists(id):
                    print ("Mã sinh viên này đã tồn tại")
                else:
                    name = get_non_empty_string("Nhập vào tên sinh viên cần thêm: ").strip()
                    theory_score = get_valid_score ("Nhập vào điểm lý thuyết cần thêm: ")
                    practice_score = get_valid_score ("Nhập vào điểm thực hành cần thêm: ")
                    assignment_score = get_valid_score ("Nhập vào điểm bài tập cần thêm: ")
                    new_student = Student(id, name, theory_score, practice_score, assignment_score)
                    Manager.add_students(new_student)
                    print (f"Đã thêm thành công sinh viên với mã sinh viên là: {id}")
            case "3":
                print ("============ Cập nhật điểm sinh viên ============")
                id = get_non_empty_string("Nhập vào mã sinh viên cần cập nhật: ").upper().strip()
                if not Manager.is_id_exists(id):
                    print ("Không tìm thấy sinh viên cần cập nhật")
                else:
                    theory_score = get_valid_score ("Nhập vào điểm lý thuyết để cập nhật: ")
                    practice_score = get_valid_score ("Nhập vào điểm thực hành để cập nhật: ")
                    assignment_score = get_valid_score ("Nhập vào điểm bài tập để cập nhật: ")
                    Manager.update_student(id, theory_score, practice_score, assignment_score)
                    print ("Đã cập nhật điểm thành công.")
            case "4":
                print ("============ Xóa sinh viên ============")
                id = get_non_empty_string("Nhập vào mã sinh viên cần xóa: ").upper().strip()
                if not Manager.is_id_exists(id):
                    print ("Không tìm thấy sinh viên cần xóa!")
                else:
                    while True:
                        choice = input(f"Bạn có chắc muốn xóa sinh viên có mã {id} này không? (Y/N): ").upper()
                        if choice in ["Y", "N"]:
                            if choice == "Y":
                                Manager.delete_student(id)
                                print ("Xóa sinh viên thành công!")
                                break
                            else:
                                print ("Đã hủy thao tác xóa")
                                break
                        else:
                            print ("Lựa chọn của bạn không hợp lệ. ")
            case "5":
                print ("============ Tìm kiếm sinh viên ============")
                name = get_non_empty_string("Nhập vào tên sinh viên cần tìm: ")
                Manager.search_student(name)
            case "6":
                print ("Thoát chương trình thành công.")
                break
            case _:
                print ("Lựa chọn của bạn không hợp lệ")
                
if __name__ == "__main__":
    main()