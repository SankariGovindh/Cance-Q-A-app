//
//  NetworkManager.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/26/19.
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
    
    init() {
        guard let url = URL(string: "http://127.0.0.1:5000/get_faqs") else { return }
        URLSession.shared.dataTask(with: url) { (data, _, _) in
            guard let data = data else { return }
            let threadData = try! JSONDecoder().decode([Thread].self, from: data)
            DispatchQueue.main.async {
                self.threadData = threadData
            }
        }.resume()
    }
}
