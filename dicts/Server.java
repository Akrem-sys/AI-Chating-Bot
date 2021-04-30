import java.io.IOException;
import java.io.*;  
import java.net.*; 
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

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
    public static void FileDelete() {
        String[] pathnames;
        String path="audios";
        File f = new File(path);
        pathnames = f.list();
        for (String pathname : pathnames) {
            File to = new File(path+"\\"+pathname);
            to.delete();
    }
}
  public static void PlayAudio(String path) throws UnsupportedAudioFileException,IOException, LineUnavailableException{
        System.out.println(path);
        AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(new File(path).getAbsoluteFile());
        Clip clip = AudioSystem.getClip();
        clip.open(audioInputStream);
        clip.start();
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
      FileDelete();
      ServerSocket serverSocket = new ServerSocket(12345);
      while(true){
      	try{
	      Socket soc = serverSocket.accept();
	      System.out.println("Receive new connection: " + soc.getInetAddress());
	      DataOutputStream dout=new DataOutputStream(soc.getOutputStream());  
	      DataInputStream in = new DataInputStream(soc.getInputStream());
	      String msg=(String)in.readUTF();
	      System.out.println("Client: "+msg);
        String audio=msg;
	      msg=FileParsing("dicts.json",msg);
	      if (msg.indexOf("Couldn't find")==-1 && audio.indexOf("PlayAudio")==-1){
		      dout.writeUTF(DefinitionFinder(msg));
		      dout.flush();
		      dout.close();
	      }

	      else if (msg.indexOf("Couldn't find")!=-1 && audio.indexOf("PlayAudio")==-1){
		      dout.writeUTF(msg);
		      dout.flush();
		      dout.close();
	      }
        else if (audio.indexOf("PlayAudio")!=-1){
          int len=audio.length();
          audio=audio.substring(10,len);
          PlayAudio(audio);
          dout.writeUTF("Playing...");
          dout.flush();
          dout.close();
        }
	    }
	    catch(Exception e){
	      e.printStackTrace(); 
  	}	}
  }
  }