import java.io.*;
import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;

public class Client1
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
				
				//q5
				BufferedReader rd = new BufferedReader (new InputStreamReader( resp.getEntity().getContent() ) );
				
				StringBuffer result = new StringBuffer();
				String line = "";
				while ((line = rd.readLine()) != null)
				{
					result.append(line);
					result.append("\n");
				}
				
				String page = result.toString();
				System.out.println(page);
				
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
