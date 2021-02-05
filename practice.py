# 도서관리 프로그램(입력 수정 삭제 출력 종료)
class lib:
    def __init__(self):
        self.ab = []
        self.check =[]
        self.menu()

    def menu(self):
        while 1:
            x= input("1.입력 2.수정 3.삭제 4.총 도서출력 5.종료 \n")
            if x=="1":  self.put_book()
            elif x=="2": self.change()
            elif x=="3": self.delete()
            elif x=="4": self.print_all()
            elif x=="5": 
                print("작동이 종료되었습니다")
                break
    
    def put_book(self):
        n=0
        name= input("도서명: ")
        while 1:
            book_num= int(input("도서번호: "))   
            if book_num not in self.check:
                print("가능한 도서번호예요")
                break
            print("이미 존재하는 도서번호예요")            
        num= input("번호: ")
        self.name= name
        self.book_num= book_num
        self.num= num
        self.ab.append([name, book_num, num]) 
        self.check.append(book_num)

    def change(self):
        c=0
        find_num= int(input("수정할 도서번호로 찾기: "))
        for i in range(0,len(self.ab)):
            if find_num == self.ab[i][1]:
                 print(self.ab[i])
                 new_name= input("수정할 도서명: ")
                 new_num= input("수정할 번호: ")
                 self.new_name = new_name
                 self.new_num = new_num
                 self.ab[i] = [new_name, self.ab[i][1], new_num] 
                 print("수정된 정보가 저장되었습니다.")
                 break
            else : c+=1
        if c==len(self.ab):
            print("존재하지 않는 도서번호입니다.")

    def delete(self):
        c=0
        find_num= int(input("삭제할 도서번호 입력: "))
        if find_num in self.check:
            for i in range(0,len(self.ab)):
                if find_num == self.ab[i][1]:
                    del self.ab[i]
                    del self.check[i]
                    print("정보가 삭제되었습니다.")
                    break
        else :
            print("도서번호가 존재하지 않습니다.")

    def print_all(self):
        print(self.ab)

    # def end_lib(self):

lib()
