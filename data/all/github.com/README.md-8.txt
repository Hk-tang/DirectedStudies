<span class="pl-k">import static</span> <span class="pl-smi">org.asynchttpclient.Dsl.*</span>;
<span class="pl-k">import</span> <span class="pl-smi">org.asynchttpclient.*</span>;
<span class="pl-k">import</span> <span class="pl-smi">io.netty.handler.codec.http.HttpHeaders</span>;

<span class="pl-k">Future<<span class="pl-smi">Integer</span>></span> whenStatusCode <span class="pl-k">=</span> asyncHttpClient<span class="pl-k">.</span>prepareGet(<span class="pl-s"><span class="pl-pds">"</span>http://www.example.com/<span class="pl-pds">"</span></span>)
.execute(<span class="pl-k">new</span> <span class="pl-k">AsyncHandler<<span class="pl-smi">Integer</span>></span>() {
	<span class="pl-k">private</span> <span class="pl-smi">Integer</span> status;
	<span class="pl-k">@Override</span>
	<span class="pl-k">public</span> <span class="pl-smi">State</span> <span class="pl-en">onStatusReceived</span>(<span class="pl-smi">HttpResponseStatus</span> <span class="pl-v">responseStatus</span>) <span class="pl-k">throws</span> <span class="pl-smi">Exception</span> {
		status <span class="pl-k">=</span> responseStatus<span class="pl-k">.</span>getStatusCode();
		<span class="pl-k">return</span> <span class="pl-smi">State</span><span class="pl-c1"><span class="pl-k">.</span>ABORT</span>;
	}
	<span class="pl-k">@Override</span>
	<span class="pl-k">public</span> <span class="pl-smi">State</span> <span class="pl-en">onHeadersReceived</span>(<span class="pl-smi">HttpHeaders</span> <span class="pl-v">headers</span>) <span class="pl-k">throws</span> <span class="pl-smi">Exception</span> {
		<span class="pl-k">return</span> <span class="pl-smi">State</span><span class="pl-c1"><span class="pl-k">.</span>ABORT</span>;
	}
	<span class="pl-k">@Override</span>
	<span class="pl-k">public</span> <span class="pl-smi">State</span> <span class="pl-en">onBodyPartReceived</span>(<span class="pl-smi">HttpResponseBodyPart</span> <span class="pl-v">bodyPart</span>) <span class="pl-k">throws</span> <span class="pl-smi">Exception</span> {
		<span class="pl-k">return</span> <span class="pl-smi">State</span><span class="pl-c1"><span class="pl-k">.</span>ABORT</span>;
	}
	<span class="pl-k">@Override</span>
	<span class="pl-k">public</span> <span class="pl-smi">Integer</span> <span class="pl-en">onCompleted</span>() <span class="pl-k">throws</span> <span class="pl-smi">Exception</span> {
		<span class="pl-k">return</span> status;
	}
	<span class="pl-k">@Override</span>
	<span class="pl-k">public</span> <span class="pl-k">void</span> <span class="pl-en">onThrowable</span>(<span class="pl-smi">Throwable</span> <span class="pl-v">t</span>) {
	}
});

<span class="pl-smi">Integer</span> statusCode <span class="pl-k">=</span> whenStatusCode<span class="pl-k">.</span>get();