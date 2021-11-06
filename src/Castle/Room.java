package castle;

import java.util.HashMap;

/*
评价一个代码的优劣并不仅仅是他能跑出来就结束了
而是在整个过程中所出现的可维护性，可扩展性【增加新的功能，代码能否尽量保持不变】，等
 */
public class Room {
    private String description;
    private HashMap<String, Room> exits = new HashMap<String, Room>();

    public void setExit(String dir, Room room){
        exits.put( dir, room);
    }

    public Room(String description) 
    {
        this.description = description;
    }

    @Override
    public String toString()
    {
        return description;
    }

    public String getExitDesc(){
        // 在这个地方的修改可以通过StringBuffer and StringBuilder 来进行操作
        // 否则系统开销会很大[ 会产生一个新的String对象 ](String不可变)
        StringBuilder sb = new StringBuilder();
        for ( String dir : exits.keySet() ) {
            sb.append(dir);
            sb.append(" ");
        }
        return sb.toString();
    }

    public Room getExit(String direction){
        // 这个函数的存在意义在于保持一个接口，以方便在未来进行对应的改变
        // 未来只需要对于接口内部的方法进行改写，而不需要对于涉及到他的所有因素进行改写
        return exits.get(direction);
    }

}
