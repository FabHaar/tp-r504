import java.io.*;
import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;

import javax.json.*;

// pour tester : ./run.sh Client2 "www.omdbapi.com/?APIKEY=751ea6aa&t=jaws"

public class Client2
{
	public static void main ( String[] args )
	{
		try 
		{
			if (args.length > 0)
			{
				
				CloseableHttpClient client = HttpClients.createDefault();
				String url = "http://" + args[0];
				HttpGet request = new HttpGet(url);
				
				//q4
				System.out.println("Executing request " + request.getRequestLine());
				CloseableHttpResponse resp = client.execute(request);
				
				System.out.println("Response Line : " + resp.getStatusLine());
				System.out.println("Response Code : " + resp.getStatusLine().getStatusCode());
				
				//client rest
				InputStreamReader isr = new InputStreamReader(resp.getEntity().getContent() );
				JsonReader reader = Json.createReader(isr);
				JsonObject jsonObject = reader.readObject();
				
				reader.close();
				isr.close();
				
				System.out.println("duree=" + jsonObject.getString("Runtime") );
			}
			else 
			{
				System.out.println("Pas d'argument fourni");
			}
		}
		catch (Exception ex) 
		{
			System.out.println("erreur !");
			ex.printStackTrace();
		}
	}
}
