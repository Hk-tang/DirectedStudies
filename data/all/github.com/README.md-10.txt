<span class="pl-smi">WebSocket</span> websocket <span class="pl-k">=</span> c<span class="pl-k">.</span>prepareGet(<span class="pl-s"><span class="pl-pds">"</span>ws://demos.kaazing.com/echo<span class="pl-pds">"</span></span>)
      .execute(<span class="pl-k">new</span> <span class="pl-smi">WebSocketUpgradeHandler</span>.<span class="pl-smi">Builder</span>()<span class="pl-k">.</span>addWebSocketListener(
          <span class="pl-k">new</span> <span class="pl-smi">WebSocketListener</span>() {

          <span class="pl-k">@Override</span>
          <span class="pl-k">public</span> <span class="pl-k">void</span> <span class="pl-en">onOpen</span>(<span class="pl-smi">WebSocket</span> <span class="pl-v">websocket</span>) {
              websocket<span class="pl-k">.</span>sendTextFrame(<span class="pl-s"><span class="pl-pds">"</span>...<span class="pl-pds">"</span></span>)<span class="pl-k">.</span>sendTextFrame(<span class="pl-s"><span class="pl-pds">"</span>...<span class="pl-pds">"</span></span>);
          }

          <span class="pl-k">@Override</span>
          <span class="pl-k">public</span> <span class="pl-k">void</span> <span class="pl-en">onClose</span>(<span class="pl-smi">WebSocket</span> <span class="pl-v">websocket</span>) {
          }
          
    		  <span class="pl-k">@Override</span>
          <span class="pl-k">public</span> <span class="pl-k">void</span> <span class="pl-en">onTextFrame</span>(<span class="pl-smi">String</span> <span class="pl-v">payload</span>, <span class="pl-k">boolean</span> <span class="pl-k">final</span><span class="pl-v">Fragment</span>, <span class="pl-k">int</span> <span class="pl-v">rsv</span>) {
          	<span class="pl-smi">System</span><span class="pl-k">.</span>out<span class="pl-k">.</span>println(payload);
          }

          <span class="pl-k">@Override</span>
          <span class="pl-k">public</span> <span class="pl-k">void</span> <span class="pl-en">onError</span>(<span class="pl-smi">Throwable</span> <span class="pl-v">t</span>) {
          }
      })<span class="pl-k">.</span>build())<span class="pl-k">.</span>get();