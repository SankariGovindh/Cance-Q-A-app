//
//  NetworkManager.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/31/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import Foundation


class NetworkManager: ObservableObject {
    var willChange = PassthroughSubject<NetworkManager, Never>()
    
    var threadData = [Thread]() {
        didSet {
            willChange.send(self)
        }
    }
    
    var dict: [Int: String] = [1: "login",
                               2: "add_user",
                               3: "add_question",
                               4: "add_comment",
                               5: "get_faqs"]
    
    init() {
        guard let url = URL(string: "http://127.0.0.1:5000/" + dict[5]!) else { return }
        URLSession.shared.dataTask(with: url) { (data, _, _) in
            guard let data = data else { return }
            let threadData = try! JSONDecoder().decode([Thread].self, from: data)
            DispatchQueue.main.async {
                self.threadData = threadData
            }
        }.resume()
    }
    
    func post(code: Int, uploadData: String) -> Bool {
        let url = URL(string: "http://127.0.0.1:5000/" + dict[code]! + uploadData)!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print ("error: \(error)")
                return
            }
            guard let response = response as? HTTPURLResponse,
                (200...299).contains(response.statusCode) else {
                print ("server error")
                return
            }
            if let mimeType = response.mimeType,
                mimeType == "application/json",
                let data = data,
                let dataString = String(data: data, encoding: .utf8) {
                print ("got data: \(dataString)")
            }
        }.resume()
        return true
    }
}
