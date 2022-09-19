import java.util.ArrayList;

class Course {
    String name;
    double hr;
    String grade;
    double points;

    Course(String name, double hr, String grade, double points) {
        this.name = name;
        this.hr = hr;
        this.grade = grade;
        this.points = points;
    }

    public String toString() {
        return this.name + "\t" + this.hr + "\t" + this.grade + "\t" + String.format("%.2f", this.points);
    }
}
class Semester {
    // BC is Simple programe, so no custom input
    public ArrayList<Course> course_list = new ArrayList<Course>();
    double gpa = 0;
    double total_hr = 0;

    private void calculate_gpa() {
        double hr_point = 0;
        double total_hr = 0;
        for ( Course course : this.course_list ) {
            hr_point += course.hr * course.points;
            total_hr += course.hr;
        }
        this.total_hr = total_hr;
        this.gpa = hr_point / total_hr;
    }

    double get_gpa() {
        if ( total_hr == 0 || gpa == 0 ) {
            this.calculate_gpa();
        } 
        if ( total_hr == 0 || gpa == 0 ) {
            System.out.println("error: data seem empty");
        } 
        return this.gpa;
    }

    public String toString() {
        String str = "";
        for (Course c : this.course_list) {
            str += c.toString();
            str += "\n";
        }
        str += "\t\t\t\t\t   GPA: " + String.format("%.2f", get_gpa()) + "\n";
        return str;
    }
}
class Account_System {
    // BC want to simplify the program, assume that the data in sem_list is entered sequentially
    public ArrayList<Semester> sem_list = new ArrayList<>();

    public String toString() {
        double total_hr_point = 0;
        double total_hr = 0;
        String str = "";
        for ( Semester sem : this.sem_list ) {
            str += "====================================================\n";
            total_hr_point += sem.get_gpa() * sem.total_hr; // BC get_gpa first so total_hr shouldn't be empty
            total_hr += sem.total_hr;
            str += sem.toString();
            str += "\t\t\t\t\t  CGPA: " + String.format("%.2f", total_hr_point / total_hr) + "\n"; 
        }
        
        return str;
    }
}

public class HW_2_2 {
    
    public static void main(String[] args) {
        // BC just a simple programe we just Combine data with programs
        Semester sem1 = new Semester();
        sem1.course_list.add(new Course("Into to Computer           ", 4.00, "A", 4.00));
        sem1.course_list.add(new Course("Programming Fundamental    ", 4.00, "A-", 3.66));
        sem1.course_list.add(new Course("Object Oriented Programming", 4.00, "B+", 3.33));

        Semester sem2 = new Semester();
        sem2.course_list.add(new Course("Databases                  ", 4.00, "A-", 3.66));
        sem2.course_list.add(new Course("Computer Networks          ", 3.00, "B-", 2.66));
        sem2.course_list.add(new Course("Web Application            ", 3.00, "B", 3.00));
        sem2.course_list.add(new Course("Operating System           ", 4.00, "C", 2.00));

        Account_System sys = new Account_System();
        sys.sem_list.add(sem1);
        sys.sem_list.add(sem2);

        System.out.println(sys);
    }
}
