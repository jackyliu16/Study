public class HW_1_4 {
    public static void main(String[] args) {
        // define a list of book
        Book[] book_list = new Book[3];
        // insert value of the book
        book_list[0] = new Book("Apple", 0, "A", "B");
        book_list[1] = new Book("Banana", 1, "C", "D");
        book_list[2] = new Book("Cat  ", 2, "E", "F");
        
        for (Book book : book_list) {
            System.out.println(book);
        }
        
        find_book_in_array(book_list, 1);
    }
        
    public static void find_book_in_array(Book[] array, int ISBN) {
        for (Book book: array) {
            if (book.ISBN == ISBN) {
                System.out.println(book);
                return;
            }
        }
        System.out.println("NOT FOUND");
    }
}

class Author {
    String name;
    String lname;
    
    Author(String name, String lname) {
        this.name = name;
        this.lname = lname;
    }
    
    public String toString() {
        // System.out.println("author name: " + this.name + " author lname: " + this.lname );
        return "\tauthor name: " + this.name + " \tauthor lname: " + this.lname ;
    }
    
    void insert_author() { }
}

class Book {
    String book_name;
    public int ISBN;
    Author author;
    
    
    Book(String book_name, int ISBN, String author_name, String author_lname) {
        this.book_name = book_name;
        this.ISBN = ISBN;
        this.author = new Author(author_name, author_lname);
    }
    
    public String toString() {
        return "book_name: " + this.book_name + this.author.toString();
    }
    
    public void insert_book() {
        System.out.println("do nothings!");
    }
    
}