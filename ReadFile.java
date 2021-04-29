package javap;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {

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
}