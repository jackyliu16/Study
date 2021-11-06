package castle;
/*
评价一个代码的优劣并不仅仅是他能跑出来就结束了
而是在整个过程中所出现的可维护性，可扩展性【增加新的功能，代码能否尽量保持不变】，等
 */
public class Room {
    private String description;
    private Room northExit;
    private Room southExit;
    private Room eastExit;
    private Room westExit;

//    public Room getNorth(){
//        return northExit;
//    }
    public Room(String description) 
    {
        this.description = description;
    }

    public void setExits(Room north, Room east, Room south, Room west) 
    {
        if(north != null)
            northExit = north;
        if(east != null)
            eastExit = east;
        if(south != null)
            southExit = south;
        if(west != null)
            westExit = west;
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
        if ( northExit != null )
            sb.append("north ");
        if ( eastExit != null )
            sb.append("east ");
        if ( westExit != null )
            sb.append("west ");
        if ( southExit != null)
            sb.append("south ");

        return sb.toString();
    }

    public Room getExit(String direction){
        Room ret = null;

        if(direction.equals("north")) {
            ret = northExit;
        }
        if(direction.equals("east")) {
            ret = eastExit;
        }
        if(direction.equals("south")) {
            ret = southExit;
        }
        if(direction.equals("west")) {
            ret = westExit;
        }


        return ret;


    }

}
