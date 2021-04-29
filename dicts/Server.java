
import java.io.*;  
import java.net.*; 
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner;

public class Server {
   long time;
   public Server(){
        this.time=0;
}
   public void start(){
		this.time=System.nanoTime();
}
   public void end(){
        double elapsedTime = (System.nanoTime() - this.time)/Math.pow(10,12);
    	System.out.printf("dexp: %f\n", elapsedTime);
}

  public static String FileParsing(String path,String word){
    try{
        File f = new File(path);
        Scanner fRead = new Scanner(f);
        while (fRead.hasNextLine()){
          String data = fRead.nextLine();
          if(data.indexOf("\""+word+"\"")!=-1){
            fRead.close();
            return data;
          }
        }
        fRead.close();
        return "Couldn't find any matching word in the dictionary";
    }catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
      return "Couldn't find any matching word in the dictionary"; 
    }}

    public static String DefinitionFinder(String data){
      return data.substring(data.indexOf("\"definition\"")+16,data.indexOf("\"__v\"")-3);
    }

  public static void main(String[] args) throws IOException{ 
      ServerSocket serverSocket = new ServerSocket(12345);
      while(true){
      	try{
	      Socket soc = serverSocket.accept();
	      System.out.println("Receive new connection: " + soc.getInetAddress());
	      DataOutputStream dout=new DataOutputStream(soc.getOutputStream());  
	      DataInputStream in = new DataInputStream(soc.getInputStream());
	      String msg=(String)in.readUTF();
	      System.out.println("Client: "+msg);
	      msg=FileParsing("dicts.json",msg);
	      if (msg.indexOf("Couldn't find")==-1){
		      dout.writeUTF(DefinitionFinder(msg));
		      dout.flush();
		      dout.close();
	      }
	    }
	    catch(Exception e){
	      e.printStackTrace(); 
  	}	}
  }
  }